class Sale:
    """Represent a bookstore sale."""

    def __init__(self, sale_id, customer_id, book_id, quantity, price):
        self.sale_id = sale_id
        self.customer_id = customer_id
        self.book_id = book_id
        self.quantity = quantity
        self.price = price
        self.total = 0

    def calculate_total(self):
        """Calculate the total price."""
        self.total = self.quantity * self.price
        return self.total

    def display_sale(self):
        """Display sale details."""
        print(f"Sale ID: {self.sale_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Book ID: {self.book_id}")
        print(f"Quantity: {self.quantity}")
        print(f"Total: €{self.total:.2f}")

    def update_quantity(self, quantity):
        """Change the quantity of books."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.quantity = quantity
        self.calculate_total()

    def get_total(self):
        """Return total sale price."""
        return self.total