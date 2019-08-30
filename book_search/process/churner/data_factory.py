from book_search.process.churner.process_bk_books_data import ProcessBXBooksData
from book_search.process.churner.recommend_books import RecommendBooks


class DataFactory:

    @staticmethod
    def get_data_object(data_type):
        data_type = data_type.lower()
        if data_type == 'bx_books':
            return globals()['ProcessBXBooksData']()

    @staticmethod
    def get_recommender_object(data_type, data_object):
        data_type = data_type.lower()
        if data_type == 'bx_books':
            return globals()['RecommendBooks'](data_object)
