
import book_search.process.utils.const as const
import book_search.process.utils.utils as utils
from book_search.process.churner.data_factory import DataFactory


class ChurnData(metaclass=utils.Singleton):

    def __init__(self, data_type):
        data_factory = DataFactory()
        self.data_object = data_factory.get_data_object(data_type)

    def correct_data(self):
        self.data_object.skim_data()


# print(books_raw.shape)
# print(users.shape)
# print(ratings.shape)
#
# print(books_raw.head())
# print(books_info.head())
#
# print(ratings.bookRating.unique())
# ratings_new = ratings[ratings.ISBN.isin(books_info.ISBN)]
# print(ratings_new)
# ratings = ratings[ratings.userID.isin(users.userID)]
#
# print(books_info.yearOfPublication.unique())
