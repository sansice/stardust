import json

import numpy
import pandas
from sklearn.neighbors import NearestNeighbors
from book_search.process.utils import const
import book_search.process.utils.utils as utils


class RecommendBooks(metaclass=utils.Singleton):

    def __init__(self, data_object):
        self.data_object = data_object
        self.rating_matrix = self._get_rating_matrix()

    def get_popular_items(self):
        ratings_explicit = self.data_object.get_explicit_ratings()
        ratings_count = pandas.DataFrame(ratings_explicit.groupby(['ISBN'])['bookRating'].sum())
        top10 = ratings_count.sort_values('bookRating', ascending=False).head(10)
        print("Following books are recommended")
        formatted_data = top10.merge(self.data_object.books_info, left_index=True, right_on='ISBN')
        # print(formatted_data)
        # return_array = []
        #
        # for item in formatted_data:
        #     print("item", formatted_data[item])
        formatted_data.columns = ["ratings", "isbn", "name", "author", "yop", "publisher"]
        formatted_data = formatted_data.applymap(str)
        return formatted_data.to_json(orient='records')

    def _get_rating_matrix(self):
        ratings_explicit = self.data_object.get_explicit_ratings()
        counts1 = ratings_explicit['userID'].value_counts()
        ratings_explicit = ratings_explicit[ratings_explicit['userID'].isin(counts1[counts1 >= 100].index)]
        counts = ratings_explicit['bookRating'].value_counts()
        ratings_explicit = ratings_explicit[ratings_explicit['bookRating'].isin(counts[counts >= 100].index)]
        ratings_matrix = ratings_explicit.pivot(index='userID', columns='ISBN', values='bookRating')
        ratings_matrix.fillna(0, inplace=True)
        ratings_matrix = ratings_matrix.astype(numpy.int32)
        return ratings_matrix

    def find_similar_users(self, user_id, metric, k):
        ratings = self.rating_matrix

        model_knn = NearestNeighbors(metric=metric, algorithm=const.bx_books_algorithm)
        model_knn.fit(ratings)
        loc = ratings.index.get_loc(user_id)
        distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors=k + 1)
        similarities = 1 - distances.flatten()

        return similarities, indices

    def find_simialr_items(self, item_id, metric, k):
        ratings = self.rating_matrix.T
        # print("ratings - ", ratings)
        # print("ratings .t - ", self.rating_matrix)
        loc = ratings.index.get_loc(item_id)
        # print("location - ", loc)
        model_knn = NearestNeighbors(metric=metric, algorithm=const.bx_books_algorithm)
        model_knn.fit(ratings)
        # print("ratings.iloc - ", ratings.iloc)
        # print("ratings.iloc[loc, :]", ratings.iloc[loc, :])
        # print("ratings.iloc[loc, :].values", ratings.iloc[loc, :].values)
        # print("ratings.iloc[loc, :].values.reshape(1, -1)", ratings.iloc[loc, :].values.reshape(1, -1))
        distances, indices = model_knn.kneighbors(ratings.iloc[loc, :].values.reshape(1, -1), n_neighbors=k + 1)
        # print("distances, indices", distances, indices)
        similarities = 1 - distances.flatten()
        print("similarities, indices", similarities, indices)
        return similarities, indices

    def predict_userbased(self, user_id, item_id, metric, k):
        ratings = self.rating_matrix
        user_loc = ratings.index.get_loc(user_id)
        item_loc = ratings.columns.get_loc(item_id)
        similarities, indices = self.find_similar_users(user_id, metric, k)  # similar users based on cosine similarity
        mean_rating = ratings.iloc[user_loc, :].mean()  # to adjust for zero based indexing
        sum_wt = numpy.sum(similarities) - 1
        wtd_sum = 0

        for i in range(0, len(indices.flatten())):
            if indices.flatten()[i] == user_loc:
                continue
            else:
                ratings_diff = ratings.iloc[indices.flatten()[i], item_loc] - numpy.mean(ratings.iloc[indices.flatten()[i], :])
                product = ratings_diff * (similarities[i])
                wtd_sum = wtd_sum + product

        prediction = int(round(mean_rating + (wtd_sum / sum_wt)))
        if prediction <= 0:
            prediction = 1
        elif prediction > 10:
            prediction = 10
        print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id, item_id, prediction))

        return prediction

    def predict_itembased(self, user_id, item_id, metric, k):
        ratings = self.rating_matrix
        wtd_sum = 0
        user_loc = ratings.index.get_loc(user_id)
        item_loc = ratings.columns.get_loc(item_id)
        similarities, indices = self.find_simialr_items(item_id, metric, k)  # similar users based on correlation coefficients
        sum_wt = numpy.sum(similarities) - 1
        for i in range(0, len(indices.flatten())):
            if indices.flatten()[i] == item_loc:
                continue
            else:
                product = ratings.iloc[user_loc, indices.flatten()[i]] * (similarities[i])
                wtd_sum = wtd_sum + product
        prediction = int(round(wtd_sum / sum_wt))

        # in case of very sparse datasets, using correlation metric for collaborative based approach may give negative ratings
        # which are handled here as below //code has been validated without the code snippet below, below snippet is to avoid negative
        # predictions which might arise in case of very sparse datasets when using correlation metric
        if prediction <= 0:
            prediction = 1
        elif prediction > 10:
            prediction = 10

        print('\nPredicted rating for user {0} -> item {1}: {2}'.format(user_id, item_id, prediction))

        return prediction

    # This function utilizes above functions to recommend items for item/user based approach and cosine/correlation.
    # Recommendations are made if the predicted rating for an item is >= to 6,and the items have not been rated already
    def recommend_item(self, user_id, item_based=True, metric='cosine', k=10):
        ratings = self.rating_matrix
        recommended_books = []
        recommended_book = {"name": "", "ratings": "", "isbn": "", "author": "", "yop": "", "publisher": ""}
        recommended_books.append(recommended_book)
        if not str(user_id).isdigit():
            print("User id is not digit")
            return recommended_books
        else:
            user_id = int(user_id)

        if user_id not in ratings.index.values:
            print("User id is not valid")
            return recommended_books

        else:
            prediction = []

            for i in range(ratings.shape[1]):
                if ratings[str(ratings.columns[i])][user_id] != 0:  # not rated already
                    if item_based:
                        prediction.append(self.predict_itembased(user_id, str(ratings.columns[i]), metric, k))
                    else:
                        prediction.append(self.predict_userbased(user_id, str(ratings.columns[i]), metric, k))
                else:
                    prediction.append(-1)  # for already rated items

            prediction = pandas.Series(prediction)
            prediction = prediction.sort_values(ascending=False)
            recommended = prediction[:10]
            for i in range(len(recommended)):
                recommended_book = {"name": self.data_object.books_info.bookTitle[recommended.index[i]],
                                    "ratings": "*****",
                                    "isbn": str(self.data_object.books_info.ISBN[recommended.index[i]]),
                                    "author": self.data_object.books_info.bookAuthor[recommended.index[i]],
                                    "yop": str(self.data_object.books_info.yearOfPublication[recommended.index[i]]),
                                    "publisher": self.data_object.books_info.publisher[recommended.index[i]]}
                recommended_books.append(recommended_book)

        return json.dumps(recommended_books)
