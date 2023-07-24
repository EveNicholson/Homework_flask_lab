from models.book import *

book1 = Book("The beach", "Alex Garland", "Adventure")
book2 = Book("Isle of joy", "Don Winslow","Thriller")
book2 = Book("Isle of joy", "Don Winslow","Thriller")
book3 = Book("Naples", "Marco Polo", "Guide")
book4 = Book("Shadow of the wind", "Ruiz Zafon", "Mystery")
book5 = Book("House of flame and shadow", "Sarah J. Mass", "Adventure")
book6 = Book("Fourth wing", "Rebecca Yarros", "Drama")
book7 = Book("Demon Copperhead", "Barbara Kingsolver", "Fantasy")
book8 = Book("An immense world", "Ed Young", "Adventure")

books=[book1, book2, book3, book4, book5, book6, book7, book8]



def add_new_book(book):
    books.append(book)

def remove_book(index):
    books.remove(index)


    

