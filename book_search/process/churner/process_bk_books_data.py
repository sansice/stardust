import copy
import numpy
import pandas
import logging
import seaborn as sns
import matplotlib.pyplot as plt

from book_search.process.churner.process_data import ProcessData
from book_search.process.utils import const

logger = logging.getLogger()


class ProcessBXBooksData(ProcessData):

    def __init__(self):
        super().__init__()
        self.books_raw = pandas.read_csv(const.bx_books_info_csv, sep=';', error_bad_lines=False, encoding=const.bx_books_encoding)
        self.books_raw.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']

        self.books_info = copy.deepcopy(self.books_raw)

        self.users = pandas.read_csv(const.bx_books_users_csv, sep=';', error_bad_lines=False, encoding=const.bx_books_encoding)
        self.users.columns = ['userID', 'Location', 'Age']

        self.ratings_raw = pandas.read_csv(const.bx_books_ratings_csv, sep=';', error_bad_lines=False, encoding=const.bx_books_encoding)
        self.ratings_raw.columns = ['userID', 'ISBN', 'bookRating']

        self.ratings = copy.deepcopy(self.ratings_raw)

    def skim_data(self):
        self.books_info.drop(['imageUrlS', 'imageUrlM', 'imageUrlL'], axis=1, inplace=True)
        self._correct_yop()
        self._correct_pub()
        self._correct_age()

    def get_explicit_ratings(self):
        ratings_explicit = self.ratings[self.ratings.bookRating != 0]
        return ratings_explicit

    def get_implicit_ratings(self):
        ratings_implicit = self.ratings[self.ratings.bookRating == 0]
        return ratings_implicit

    def _correct_pub(self):
        self.books_info.loc[(self.books_info.ISBN == '193169656X'), 'publisher'] = 'other'
        self.books_info.loc[(self.books_info.ISBN == '1931696993'), 'publisher'] = 'other'

    def _correct_ratings(self):
        self.ratings = self.ratings_raw[self.ratings_raw.ISBN.isin(self.books_info.ISBN)]

    def check_sparcity(self):
        ratings_new = self.ratings[self.ratings.ISBN.isin(self.books_info.ISBN)]
        n_books = len(self.books_info)
        n_users = len(self.users)
        sparsity = 1.0 - len(ratings_new) / float(n_users * n_books)
        return sparsity * 100

    def _correct_age(self):
        self.users.loc[(self.users.Age > 90) | (self.users.Age < 5), 'Age'] = numpy.nan
        self.users.Age = self.users.Age.fillna(self.users.Age.mean())
        self.users.Age = self.users.Age.astype(numpy.int32)

    def _correct_yop(self):
        self.books_info.loc[self.books_info.ISBN == '0789466953', 'yearOfPublication'] = 2000
        self.books_info.loc[self.books_info.ISBN == '0789466953', 'bookAuthor'] = "James Buckley"
        self.books_info.loc[self.books_info.ISBN == '0789466953', 'publisher'] = "DK Publishing Inc"
        self.books_info.loc[
            self.books_info.ISBN == '0789466953', 'bookTitle'] = "DK Readers: Creating the X-Men, How Comic Books Come to Life (Level 4: Proficient Readers)"

        self.books_info.loc[self.books_info.ISBN == '078946697X', 'yearOfPublication'] = 2000
        self.books_info.loc[self.books_info.ISBN == '078946697X', 'bookAuthor'] = "Michael Teitelbaum"
        self.books_info.loc[self.books_info.ISBN == '078946697X', 'publisher'] = "DK Publishing Inc"
        self.books_info.loc[
            self.books_info.ISBN == '078946697X', 'bookTitle'] = "DK Readers: Creating the X-Men, How It All Began (Level 4: Proficient Readers)"

        self.books_info.loc[self.books_info.ISBN == '2070426769', 'yearOfPublication'] = 2003
        self.books_info.loc[self.books_info.ISBN == '2070426769', 'bookAuthor'] = "Jean-Marie Gustave Le ClÃ?Â©zio"
        self.books_info.loc[self.books_info.ISBN == '2070426769', 'publisher'] = "Gallimard"
        self.books_info.loc[self.books_info.ISBN == '2070426769', 'bookTitle'] = "Peuple du ciel, suivi de 'Les Bergers"
        self.books_info.yearOfPublication = pandas.to_numeric(self.books_info.yearOfPublication, errors='coerce')
        self.books_info.loc[(self.books_info.yearOfPublication > 2006) | (self.books_info.yearOfPublication == 0), 'yearOfPublication'] = numpy.NAN
        self.books_info.yearOfPublication.fillna(round(self.books_info.yearOfPublication.mean()), inplace=True)
        self.books_info.yearOfPublication = self.books_info.yearOfPublication.astype(numpy.int32)

    def plot_ratings(self):
        sns.countplot(data=self.get_explicit_ratings(), x='bookRating')
        plt.show()

    def print_data(self):
        # unique_yop = self.books_info.yearOfPublication.unique()
        # print(unique_yop)
        books_yop_null = self.books_info.yearOfPublication.isnull().sum()
        print('The number of year of pub null are - {books_yop_null}'.format(books_yop_null=books_yop_null))

        books_pub_null = len(self.books_info.loc[self.books_info.publisher.isnull(), :])
        print('The number of pub null are - {books_pub_null}'.format(books_pub_null=books_pub_null))

        users_age_null = self.users.Age.isnull().sum()
        print('The number of users with age null are - {users_age_null}'.format(users_age_null=users_age_null))