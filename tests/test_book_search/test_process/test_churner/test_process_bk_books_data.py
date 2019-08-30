import os
import unittest


from book_search.process.churner.process_bk_books_data import ProcessBXBooksData


class TestProcessBXBooksData(unittest.TestCase):

    def setUp(self):
        self.bk_books_data_processor = ProcessBXBooksData()

    def tearDown(self) -> None:
        pass

    def test_skim_data(self):
        # self.bk_books_data_processor.print_data()
        self.bk_books_data_processor.skim_data()
        self.bk_books_data_processor.print_data()
        sparsity = self.bk_books_data_processor.check_sparcity()
        print(sparsity)

    # def test_check_sparcity(self):
    #     pass
    #     self.bk_books_data_processor.plot_ratings()

    def test_get_explicit_ratings(self):
        explicit_ratings = self.bk_books_data_processor.get_explicit_ratings()
        print(explicit_ratings)


if __name__ == '__main__':
    unittest.main()
