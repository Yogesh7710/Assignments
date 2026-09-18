import csv
from Book import Book
from Customers import Customer
from Sales import Sale

class Bookstore:
    """Manage the bookstore."""

    def __init__(self):
        self.books = []
        self.customers = []
        self.sales = []

    # ---------- BOOK METHODS ----------

    def add_book(self, book):
        """Add a book."""
        self.books.append(book)
        print("Book added successfully.")

    def show_books(self):
        """Display all books."""
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            print("----------------------------")
            book.display_book()

    def search_book(self, title):
        """Search for a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None

    def remove_book(self, book_id):
        """Remove a book."""
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed.")
                return

        print("Book not found.")

    # ---------- CUSTOMER METHODS ----------

    def add_customer(self, customer):
        """Add a customer."""
        self.customers.append(customer)
        print("Customer registered successfully.")

    def show_customers(self):
        """Display all customers."""
        if not self.customers:
            print("No customers found.")
            return

        for customer in self.customers:
            print("----------------------------")
            customer.display_customer()

    def search_customer(self, customer_id):
        """Find a customer."""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer

        return None

    # ---------- SALES METHODS ----------

    def make_sale(self, customer_id, book_id, quantity):
        """Create a new sale."""

        customer = self.search_customer(customer_id)

        if customer is None:
            print("Customer not found.")
            return

        book = None

        for item in self.books:
            if item.book_id == book_id:
                book = item
                break

        if book is None:
            print("Book not found.")
            return

        try:
            book.remove_stock(quantity)
        except ValueError as error:
            print(error)
            return

        sale_id = len(self.sales) + 1

        sale = Sale(
            sale_id,
            customer_id,
            book_id,
            quantity,
            book.price
        )

        sale.calculate_total()

        self.sales.append(sale)
        customer.add_purchase(sale_id)

        print("Sale completed successfully.")
        print(f"Total: €{sale.total:.2f}")

    def show_sales(self):
        """Display all sales."""
        if not self.sales:
            print("No sales found.")
            return

        for sale in self.sales:
            print("----------------------------")
            sale.display_sale()

    # ---------- FILE HANDLING ----------

    def load_books(self):
        """Load books from CSV."""
        try:
            with open("all_files/books.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.books.append(
                        Book(
                            row["book_id"],
                            row["title"],
                            row["author"],
                            float(row["price"]),
                            int(row["quantity"]),
                            row["category"]
                        )
                    )
        except FileNotFoundError:
            print("No books file found. Starting fresh.")

    def load_customers(self):
        """Load customers from CSV."""
        try:
            with open("all_files/customers.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.customers.append(
                        Customer(
                            row["customer_id"],
                            row["name"],
                            row["email"],
                            row["phone"]
                        )
                    )
        except FileNotFoundError:
            print("No customers file found. Starting fresh.")

    def load_sales(self):
        """Load sales from CSV."""
        try:
            with open("all_files/sales.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    sale = Sale(
                        row["sale_id"],
                        row["customer_id"],
                        row["book_id"],
                        int(row["quantity"]),
                        float(row["total"]) / int(row["quantity"])
                    )
                    sale.total = float(row["total"])
                    self.sales.append(sale)
        except FileNotFoundError:
            print("No sales file found. Starting fresh.")

    def save_books(self):
        """Save books to CSV."""
        with open("all_files/books.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "book_id",
                "title",
                "author",
                "price",
                "quantity",
                "category"
            ])

            for book in self.books:
                writer.writerow([
                    book.book_id,
                    book.title,
                    book.author,
                    book.price,
                    book.quantity,
                    book.category
                ])

    def save_customers(self):
        """Save customers to CSV."""
        with open("all_files/customers.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "customer_id",
                "name",
                "email",
                "phone"
            ])

            for customer in self.customers:
                writer.writerow([
                    customer.customer_id,
                    customer.name,
                    customer.email,
                    customer.phone
                ])

    def save_sales(self):
        """Save sales to CSV."""
        with open("all_files/sales.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "sale_id",
                "customer_id",
                "book_id",
                "quantity",
                "total"
            ])

            for sale in self.sales:
                writer.writerow([
                    sale.sale_id,
                    sale.customer_id,
                    sale.book_id,
                    sale.quantity,
                    sale.total
                ])

    def save_all(self):
        """Save all data."""
        self.save_books()
        self.save_customers()
        self.save_sales()
        print("All data saved successfully.")
