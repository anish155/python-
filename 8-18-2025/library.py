from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available"
        self.due_date = None

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            self.due_date = datetime.now() + timedelta(days=20)
            print(f"📚 '{self.title}' by {self.author} has been borrowed. Return by {self.due_date.date()}.")
        else:
            print(f"❌ '{self.title}' is already borrowed. Due on {self.due_date.date()}.")

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            self.due_date = None
            print(f"✅ '{self.title}' has been returned and is now available.")
        else:
            print(f"❌ '{self.title}' was not borrowed.")

    def show_info(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")
        if self.status == "borrowed":
            print(f"Due Date: {self.due_date.date()}")
        print("-" * 30)


library = [
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald")
]

while True:
    print("\n======= Library Menu =======")
    print("1. Show All Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\n--- Book List ---")
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. {book.title} by {book.author} ({book.status})")
        print("------------------")

    elif choice == "2":
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. {book.title} ({book.status})")
        select = int(input("Select book number to borrow: "))
        if 1 <= select <= len(library):
            library[select-1].borrow()
        else:
            print("❌ Invalid choice.")

    elif choice == "3":
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. {book.title} ({book.status})")
        select = int(input("Select book number to return: "))
        if 1 <= select <= len(library):
            library[select-1].return_book()
        else:
            print("❌ Invalid choice.")

    elif choice == "4":
        print("🙏 Thank you for using the library system!")
        break

    else:
        print("❌ Invalid option, try again.")
