#!/usr/bin/env python3
"""
A module for a library system demonstrating inheritance and composition.
"""

class Book:
    """
    Base class for a book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title, author):
        """Initializes the Book with a title and an author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    A derived class for an electronic book, inheriting from Book.

    Attributes:
        file_size (int): The file size of the ebook in KB.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes the EBook, calling the base class constructor.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a user-friendly string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A derived class for a physical book, inheriting from Book.

    Attributes:
        page_count (int): The total number of pages in the book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes the PrintBook, calling the base class constructor.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a user-friendly string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class representing a library, which is composed of books.

    Attributes:
        books (list): A list to store book objects.
    """
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a book object (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book currently in the library."""
        for book in self.books:
            print(book)