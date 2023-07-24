import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book1 = Book("The beach", "Alex Garland", "Adventure")
        self.book2 = Book("Providence", "Caroline Kepnes", "Drama")
        self.book3 = Book("Naples", "Marco Polo", "Guide")
        self.book4 = Book("Shadow of the wind", "Ruiz Zafon", "Mystery")
        self.book5 = Book("House of flame and shadow", "Sarah J. Mass", "Adventure")
        self.book6 = Book("Fourth wing", "Rebecca Yarros", "Drama")
        self.book7 = Book("Demon Copperhead", "Barbara Kingsolver", "Fantasy")
        self.book8 = Book("An immense world", "Ed Young", "Adventure")
    
        self.library=[self.book1, self.book2, self.book3, self.book4, self.book5, self.book6, self.book7, self.book8]

        def test_library_has_a_book(self):
            self.assertEqual("The beach", "Alex Garland", "Adventure",)

        def test_show_all_books(self):
            self.assertEqual(self.library)
           
        def test_add_new_book(self):
            self.assertEqual(self.library.book)   
   
        def test_remove_book(self):
            self.assertEqual(self.library.book)  


   
                        