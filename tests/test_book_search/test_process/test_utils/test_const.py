import os
import unittest


import book_search.process.utils.const as const


class TestUnittestGenerator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    def test_project_path(self):
        project_home = const.project_home
        print(project_home)
        self.assertTrue(os.path.exists(project_home))
        pass

    def test_sub_project_path(self):
        sub_project_home = const.sub_project_home
        print(sub_project_home)
        self.assertTrue(os.path.exists(sub_project_home))
        pass

    def test_project_data_path(self):
        data_path = const.data_path
        print(data_path)
        self.assertTrue(os.path.exists(data_path))
        pass

    def test_bx_books_csv_path(self):
        bx_books_csv_path = const.bx_books_csv_path
        print(bx_books_csv_path)
        self.assertTrue(os.path.exists(bx_books_csv_path))
        pass

    def test_bx_books_ratings_csv(self):
        bx_books_ratings_csv = const.bx_books_ratings_csv
        print(bx_books_ratings_csv)
        self.assertTrue(os.path.isfile(bx_books_ratings_csv))
        self.assertTrue(os.path.exists(bx_books_ratings_csv))
        pass

    def test_bx_books_info_csv(self):
        bx_books_info_csv = const.bx_books_info_csv
        print(bx_books_info_csv)
        self.assertTrue(os.path.isfile(bx_books_info_csv))
        self.assertTrue(os.path.exists(bx_books_info_csv))
        pass

    def test_bx_books_users_csv(self):
        bx_books_users_csv = const.bx_books_users_csv
        print(bx_books_users_csv)
        self.assertTrue(os.path.isfile(bx_books_users_csv))
        self.assertTrue(os.path.exists(bx_books_users_csv))
        pass


if __name__ == '__main__':
    unittest.main()
