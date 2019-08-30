import os
import unittest


import book_search.process.churner.churn_data as const
from book_search.process.churner.churn_data import ChurnData


class TestChurnData(unittest.TestCase):

    def setUp(self):
        self.churn_data = ChurnData('bx_books')

    def tearDown(self) -> None:
        pass

    def test_its_singleton(self):
        churn_data_1 = ChurnData('bx_books')
        churn_data_2 = ChurnData('bx_boo2ks')

        self.assertEqual(churn_data_1, churn_data_2)


if __name__ == '__main__':
    unittest.main()
