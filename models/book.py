class Book():

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre= genre
        self.library=[]
    
    def show_all_books(self,library):
        for self.book in self.library:
            return(self.book)

    def add_new_book(self,book):
        self.library.append(book)

    def remove_book(self,book):
        self.library.remove(book)

    