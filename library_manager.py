import os
import json
from rich import print
from rich.console import Console
from rich.text import Text

# Define the library as a list of dictionaries
library = []

# Initialize the console object
console = Console()

# Function to save the library to a file
def save_library():
    with open('library.txt', 'w') as file:
        json.dump(library, file)
    console.print("📚 Library saved to file. Goodbye!", style="bold green")

# Function to load the library from a file
def load_library():
    global library
    if os.path.exists('library.txt'):
        with open('library.txt', 'r') as file:
            library = json.load(file)
        console.print("📚 Library loaded from file.", style="bold blue")
    else:
        console.print("📚 No saved library found.", style="bold yellow")

# Function to display the library statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book['Read Status'])
    percentage_read = (read_books / total_books) * 100 if total_books else 0
    console.print(f"📊 Total books: {total_books}", style="bold cyan")
    console.print(f"📖 Percentage read: {percentage_read:.2f}%", style="bold magenta")

# Function to display all books in the library
def display_all_books():
    if not library:
        console.print("📚 Your library is empty!", style="bold red")
    else:
        console.print("📚 Your Library:", style="bold yellow")
        for idx, book in enumerate(library, 1):
            read_status = "✅ Read" if book['Read Status'] else "❌ Unread"
            console.print(f"{idx}. [bold]{book['Title']}[/bold] by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {read_status}", style="bold green")

# Function to search for a book by title or author
def search_for_book():
    console.print("🔍 Search by:", style="bold purple")
    console.print("1. Title", style="bold")
    console.print("2. Author", style="bold")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter the *book title* (in *bold*): ").lower()
        found_books = [book for book in library if title in book['Title'].lower()]
    elif choice == '2':
        author = input("Enter the _author's name_ (in _italic_): ").lower()
        found_books = [book for book in library if author in book['Author'].lower()]
    else:
        console.print("❌ Invalid choice.", style="bold red")
        return
    
    if found_books:
        console.print("📚 Matching Books:", style="bold blue")
        for idx, book in enumerate(found_books, 1):
            read_status = "✅ Read" if book['Read Status'] else "❌ Unread"
            console.print(f"{idx}. [bold]{book['Title']}[/bold] by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {read_status}", style="bold green")
    else:
        console.print("📚 No matching books found.", style="bold red")

# Function to remove a book by title
def remove_book():
    title = input("🗑️ Enter the *title* of the book to remove: ").lower()
    global library
    library = [book for book in library if title.lower() not in book['Title'].lower()]
    console.print("🗑️ Book removed successfully!", style="bold green")

# Function to add a new book
def add_book():
    title = input("📚 Enter the *book title* (in *bold*): ")
    author = input("🖋️ Enter the _author_ (in _italic_): ")
    publication_year = int(input("📅 Enter the *publication year* (in *bold*): "))
    genre = input("📖 Enter the *genre* (in *bold*): ")
    read_status_input = input("📘 Have you read this book? (yes/no): ").lower()
    read_status = True if read_status_input == 'yes' else False
    
    book = {
        'Title': title,
        'Author': author,
        'Publication Year': publication_year,
        'Genre': genre,
        'Read Status': read_status
    }
    
    library.append(book)
    console.print("📚 Book added successfully!", style="bold green")

# Function to display the menu and handle user choices
def menu():
    while True:
        console.print("\n🔖 Menu", style="bold cyan")
        console.print("Welcome to your Personal Library Manager! 📚", style="bold yellow")
        console.print("1. Add a book 📚", style="bold green")
        console.print("2. Remove a book 🗑️", style="bold red")
        console.print("3. Search for a book 🔍", style="bold blue")
        console.print("4. Display all books 📖", style="bold purple")
        console.print("5. Display statistics 📊", style="bold magenta")
        console.print("6. Exit 🚪", style="bold yellow")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_for_book()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            save_library()
            console.print("🚪 Goodbye!", style="bold red")
            break
        else:
            console.print("❌ Invalid choice. Please try again.", style="bold red")

# Main function to start the program
def main():
    load_library()
    menu()

if __name__ == '__main__':
    main()
