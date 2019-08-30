import pandas


class RecommendBooks(object):

    def __init__(self, data_object):
        self.data_object = data_object

    def get_popular_items(self):
        ratings_explicit = self.data_object.get_explicit_ratings()
        ratings_count = pandas.DataFrame(ratings_explicit.groupby(['ISBN'])['bookRating'].sum())
        top10 = ratings_count.sort_values('bookRating', ascending=False).head(10)
        print("Following books are recommended")
        formatted_data = top10.merge(self.data_object.books_info, left_index=True, right_on='ISBN')
        print(formatted_data)
        return formatted_data.to_html()
