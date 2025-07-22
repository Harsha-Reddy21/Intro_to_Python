library = []

def add_book(title, author):
    book = {
        "title": title.strip().title(),
        "author": author.strip().title()
    }
    library.append(book)
    print(f'Book "{book["title"]}" by {book["author"]} added.')

def search_book(title):
    found = False
    for book in library:
        if book["title"] == title.strip().title():
            print(f'Found: "{book["title"]}" by {book["author"]}')
            found = True
            break
    if not found:
        print(f'Book titled "{title}" not found.')

def display_inventory():
    if not library:
        print("Library inventory is empty.")
    else:
        print("\nLibrary Inventory:")
        for idx, book in enumerate(library, 1):
            print(f'{idx}. "{book["title"]}" by {book["author"]}')
        print()

def main():
    print("Welcome to the Simple Library Management System")

    while True:
        print("\nChoose an option:")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)

        elif choice == "2":
            title = input("Enter title to search: ")
            search_book(title)

        elif choice == "3":
            display_inventory()

        elif choice == "4":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
