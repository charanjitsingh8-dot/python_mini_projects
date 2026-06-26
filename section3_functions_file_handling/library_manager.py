import csv
import os

filename = "books.csv"

def initialize_file():
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Year"])

def load_books():
    books = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        print("Books file not found. Starting fresh.")
    return books

def save_books(books):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Year"])
        writer.writeheader()
        writer.writerows(books)

def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    books.append({"Title": title, "Author": author, "Year": year})
    save_books(books)
    print(f"'{title}' added successfully.")

def remove_book(books):
    title = input("Enter book title to remove: ").strip()
    found = [book for book in books if book["Title"].lower() == title.lower()]
    if not found:
        print("Book not found.")
        return books
    books = [book for book in books if book["Title"].lower() != title.lower()]
    save_books(books)
    print(f"'{title}' removed successfully.")
    return books

def search_book(books):
    title = input("Enter book title to search: ").strip()
    results = [book for book in books if title.lower() in book["Title"].lower()]
    if results:
        print("\n" + "=" * 40)
        for book in results:
            print(f"  Title  : {book['Title']}")
            print(f"  Author : {book['Author']}")
            print(f"  Year   : {book['Year']}")
            print("-" * 40)
    else:
        print("No matching books found.")

def show_all_books(books):
    if not books:
        print("No books in the library.")
        return
    print("\n" + "=" * 40)
    print("         ALL BOOKS")
    print("=" * 40)
    for book in books:
        print(f"  Title  : {book['Title']}")
        print(f"  Author : {book['Author']}")
        print(f"  Year   : {book['Year']}")
        print("-" * 40)

def main():
    initialize_file()
    books = load_books()

    print("=" * 40)
    print("   Library Book Management System")
    print("=" * 40)

    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            books = remove_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            show_all_books(books)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()