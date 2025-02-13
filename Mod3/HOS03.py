# HOS03.py - A program to manage a list of books in a library using a list of dictionaries  

def add_books(book_list, book):
    book_list.append(book)  # Add the book to the list  
    print(f"Book '{book}' has been added to the list.") # Confirmation message  
    
# Example usage:

def remove_books(book_list, title):
    for book in book_list:  # Iterate through the list to find the book to remove
        if book ['0'] == title:

            book_list.remove(book)  # Remove the book from the list 
            print(f"Removed book:{title}")  
            return  
        #  Confirmation message
    print ("Book Not Found.")   # If the book is not found in the list  
    
def search_book(book_list, title):
    for book in book_list:  # Iterate through the list to find the book
        if book[0] == title:
            print(f"Found book: {title}")
            return
    print("Book Not Found.")

def convert_to_tuples(book_list):

    return [tuple(book ) for book in book_list]    #  Convert each dictionary to a tuple and return a list of tuples

def convert_to_lists(tuple_list):   # Convert each tuple to a list and return a list of lists
    return [list(t) for t in tuple_list]
books_list = [
    ["1984", "George Orwell"],
    ["To Kill a Mockingbird", "Harper Lee"]
]
# Removed erroneous call to remove_books as it used an undefined variable.
books_tuples = convert_to_tuples(books_list)  # Convert the list of books to a list of tuples   

books_list_modifiable = convert_to_lists(books_tuples)  # Convert the list of tuples back to a list of lists    

# The erroneous call to undefined function "add_book" has been removed.
add_books  (books_list_modifiable, ["A Brief History of Time", "Stephen Hawking"])  # Add a new book to the list 
remove_books (books_list_modifiable, "1984")  # Remove a book from the list
 
print ("Final books list:") 
for book in books_list_modifiable:  
    print (book) # Print the final list of books        
 
 