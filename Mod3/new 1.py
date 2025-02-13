BOOK_NOT_FOUND = "Book Not Found"

def remove_book(books, title):
    """
    Removes a book from the list of books based on its title.

    Args:
        books: A list of dictionaries, where each dictionary represents a book.
        title: The title of the book to be removed.

    Returns:
        The updated list of books if the book is found,
        or the constant BOOK_NOT_FOUND if the book is not found.
    """
    for book in books:
        if book['title'] == title:
            books.remove(book)
            return books  # Return early after successful removal
    return BOOK_NOT_FOUND

# Example usage:
books = [
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen'}
]

# Attempt to remove a book
updated_books = remove_book(books, "1984")

if updated_books == BOOK_NOT_FOUND:
    print("Book not found.")
else:
    print("Book removed successfully.")
    # Print the updated list (if the book was found)
    for book in updated_books:
        print(f"Title: {book['title']}, Author: {book['author']}")