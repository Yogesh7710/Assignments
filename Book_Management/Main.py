from Book import Book
from Customers import Customer
from Bookstore import Bookstore


def main():
    """Start the bookstore management system."""

    store = Bookstore()
    store.load_books()
    store.load_customers()
    store.load_sales()

    # Sample books
    store.add_book(
        Book(
            1,
            "Harry Potter",
            "J.K. Rowling",
            15.99,
            10,
            "Fantasy"
        )
    )

    store.add_book(
        Book(
            2,
            "Atomic Habits",
            "James Clear",
            18.50,
            8,
            "Self Help"
        )
    )

    # Sample customer
    store.add_customer(
        Customer(
            1,
            "James Bond",
            "bond.james@email.com",
            "123456789"
        )
    )

    while True:

        print("\n================================")
        print("    BOOKSTORE MANAGEMENT SYSTEM")
        print("================================")
        print("1. View Books")
        print("2. Search Book")
        print("3. Add Book")
        print("4. Remove Book")
        print("5. View Customers")
        print("6. Register Customer")
        print("7. Make Sale")
        print("8. View Sales")
        print("9. Save Data")
        print("10. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                store.show_books()

            elif choice == "2":
                title = input("Enter book title: ")

                book = store.search_book(title)

                if book:
                    book.display_book()
                else:
                    print("Book not found.")

            elif choice == "3":
                book_id = int(input("Enter book ID: "))
                title = input("Enter title: ")
                author = input("Enter author: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                category = input("Enter category: ")

                book = Book(
                    book_id,
                    title,
                    author,
                    price,
                    quantity,
                    category
                )

                store.add_book(book)

            elif choice == "4":
                book_id = int(input("Enter book ID: "))
                store.remove_book(book_id)

            elif choice == "5":
                store.show_customers()

            elif choice == "6":
                customer_id = int(
                    input("Enter customer ID: ")
                )

                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")

                customer = Customer(
                    customer_id,
                    name,
                    email,
                    phone
                )

                store.add_customer(customer)

            elif choice == "7":
                customer_id = int(
                    input("Enter customer ID: ")
                )

                book_id = int(
                    input("Enter book ID: ")
                )

                quantity = int(
                    input("Enter quantity: ")
                )

                store.make_sale(
                    customer_id,
                    book_id,
                    quantity
                )

            elif choice == "8":
                store.show_sales()

            elif choice == "9":
                store.save_all()

            elif choice == "10":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid information.")


if __name__ == "__main__":
    main()