import os
import unittest


from book_search.process.churner.process_bk_books_data import ProcessBXBooksData
from book_search.process.churner.recommend_books import RecommendBooks


class TestRecommendBooks(unittest.TestCase):

    def setUp(self):
        bk_books_data_processor = ProcessBXBooksData()
        bk_books_data_processor.skim_data()
        self.recommend_books = RecommendBooks(bk_books_data_processor)

    def tearDown(self) -> None:
        pass

    def test_get_popular_books(self):
        # self.bk_books_data_processor.print_data()
        self.recommend_books.get_popular_items()


if __name__ == '__main__':
    unittest.main()
