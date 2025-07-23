#Q 2: Create a class to represent a book with attributes like title, author, and publication year.

class Book:
    def __init__(self):
        self.addition = {}

    def bookLibraries(self):
        book_name = input("Enter the book name: ")
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        publication = int(input("Enter the publication year: "))

        if book_name in self.addition:
            print(f"The book '{book_name}' is already in the collection.")
        else:
            self.addition[book_name] = {
                'title': title,
                'author': author,
                'publication': publication
            }
            print(f"The book '{book_name}' has been added successfully.")

    def showBooks(self):
        if not self.addition:
            print("no book available.")
        else:
            print("books details:")
            for book_name,details in self.addition.items():
                print("Books details:")
                for book_name, details in self.addition.items():
                    print(f"Book Name: {book_name}")
                    print(f"Title: {details['title']}")
                    print(f"Author: {details['author']}")
                    print(f"Publication Year: {details['publication']}")
library = Book()

while True:
    print("1.add the book:")
    print("2.show the book list:")
    print("3.exit:")
    try:
        choice = int(input("enter the choice:"))
        if choice == 1:
            library.bookLibraries()
        elif choice == 2:
            library.showBooks()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
        continue
