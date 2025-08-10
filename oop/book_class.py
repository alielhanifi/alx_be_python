# oop/book_class.py

class Book:
    """
    A simple Book model with magic methods.
    Attributes:
        title (str): Title of the book
        author (str): Author of the book
        year (int): Publication year
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = int(year)

    def __str__(self) -> str:
        # User-friendly representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # Official, reproducible representation
        # Using !r ensures proper quoting for strings
        return f"Book({self.title!r}, {self.author!r}, {self.year})"

    def __del__(self):
        # Avoid any exceptions during interpreter shutdown
        try:
            print(f"Deleting {self.title}")
        except Exception:
            pass
