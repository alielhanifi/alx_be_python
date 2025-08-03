#!/usr/bin/python3
"""
This module defines the Book and Library classes for a simple library management system.
"""

class Book:
    """
    Represents a single book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available) if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)

    def _find_book(self, title):
        """Private helper method to find a book by its title."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Checks out a book by its title, making it unavailable.
        """
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"Checked out '{title}'.")
            else:
                print(f"'{title}' is already checked out.")
        else:
            print(f"Error: Book with title '{title}' not found.")

    def return_book(self, title):
        """
        Returns a book by its title, making it available again.
        """
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"Returned '{title}'.")
            else:
                print(f"'{title}' was not checked out.")
        else:
            print(f"Error: Book with title '{title}' not found.")

    def list_available_books(self):
        """
        Prints a list of all books that are currently available.
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No available books.")
            return

        for book in available_books:
            print(f"{book.title} by {book.author}")