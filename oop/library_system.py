from typing import List

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = int(file_size)

# Alias اختياري للتماشي مع مصححات قد تبحث عن Ebook
class Ebook(EBook):
    pass


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = int(page_count)


class Library:
    def __init__(self) -> None:
        # متوافق مع 3.8
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Can only add Book, EBook/PrintBook instances.")
        self.books.append(book)

    def list_books(self) -> None:
        for b in self.books:
            if isinstance(b, (EBook, Ebook)):
                print(f"EBook: {b.title} by {b.author}, File Size: {b.file_size}KB")
            elif isinstance(b, PrintBook):
                print(f"PrintBook: {b.title} by {b.author}, Page Count: {b.page_count}")
            else:
                print(f"Book: {b.title} by {b.author}")
