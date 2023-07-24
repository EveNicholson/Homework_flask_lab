import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("The beach", "Alex Garland", "Adventure")

    def test_book_has_title(self):
        self.assertEqual("The beach", self.book.title)

    def test_book_has_author(self):
        self.assertEqual("Alex Garland", self.book.author)

    def test_book_has_genre(self):
        self.assertEqual("Adventure", self.book.genre)

    
                        