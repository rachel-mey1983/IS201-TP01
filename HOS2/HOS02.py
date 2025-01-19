from dbm.ndbm import library
from enum import Enum
from pty import CHILD

class Category (Enum):
    FICTION = 1
    NONFICTION = 2
    EDUCATIONAL = 3
    CHILDREN = 4
    
class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.category.name})"
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self, category=None):
        if category:
            return [book for book in self.books if book.category == category]
        return self.books
    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", Category.FICTION)
    book2 = Book("The Da Vinci Code", "Dan Brown", Category.FICTION)
    
    fiction_category_number = 1
    fiction_category_enum = Category(fiction_category_number)
    book3 = Book("The Catcher in the Rye", "J.D. Salinger", fiction_category_enum)  
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()

