class Customer:
    """Represent a bookstore customer."""

    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.purchases = []

    def display_customer(self):
        """Display customer details."""
        print(f"ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")

    def update_customer(self, name, email, phone):
        """Update customer information."""
        self.name = name
        self.email = email
        self.phone = phone

    def add_purchase(self, sale_id):
        """Add a sale to purchase history."""
        self.purchases.append(sale_id)

    def show_history(self):
        """Display purchase history."""
        if not self.purchases:
            print("No purchases found.")
        else:
            for sale_id in self.purchases:
                print(f"Sale ID: {sale_id}")