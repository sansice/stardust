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
        return_str = self.recommend_books.get_popular_items()
        print(return_str)

    # def find_similar_users(self):
    #     # self.bk_books_data_processor.print_data()
    #     similarities, indices = self.recommend_books.find_similar_users(11676)
    #     print(similarities)
    #     print(indices)

    # def test_predict_userbased(self):
    #     # self.bk_books_data_processor.print_data()
    #     prediction = self.recommend_books.predict_userbased(11676, '0001056107')
    #     print(prediction)

    # def test_predict_itembased(self):
    #     # self.bk_books_data_processor.print_data()
    #     prediction = self.recommend_books.predict_itembased(11676, '0001056107')
    #     print(prediction)

    # def test_recommend_item(self):
    #     # self.bk_books_data_processor.print_data()
    #     # prediction = self.recommend_books.recommend_item(4385)
    #     # print(prediction)
    #     # prediction = self.recommend_books.recommend_item(4385, False)
    #     # print(prediction)
    #     prediction = self.recommend_books.recommend_item(4385, True, metric='correlation')
    #     print(prediction)
    #     # prediction = self.recommend_books.recommend_item(4385, False, metric='correlation')
    #     # print(prediction)


if __name__ == '__main__':
    testsuite = TestRecommendBooks()
    testsuite.test_recommend_item()
