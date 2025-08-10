# oop/book_class.py

class Book:
    """Simple Book class demonstrating magic methods."""
    def __init__(self, title, author, year):
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Exact spacing and quoting per spec
        return "Book({!r}, {!r}, {})".format(self.title, self.author, self.year)

    def __del__(self):
        print(f"Deleting {self.title}")
