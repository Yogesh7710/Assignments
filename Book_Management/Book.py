class Book:
    """Represent a book in the bookstore."""

    def __init__(self, book_id, title, author, price, quantity, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.category = category

    def display_book(self):
        """Display book details."""
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: €{self.price:.2f}")
        print(f"Stock: {self.quantity}")
        print(f"Category: {self.category}")

    def update_book(self, title, author, price, category):
        """Update book details."""
        self.title = title
        self.author = author
        self.price = price
        self.category = category

    def add_stock(self, quantity):
        """Add books to stock."""
        self.quantity += quantity

    def remove_stock(self, quantity):
        """Remove books from stock."""
        if quantity > self.quantity:
            raise ValueError("Not enough stock.")

        self.quantity -= quantity