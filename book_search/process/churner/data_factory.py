from book_search.process.churner.process_bk_books_data import ProcessBXBooksData


class DataFactory:

    @staticmethod
    def get_data_object(data_type):
        data_type = data_type.lower()
        if data_type == 'bx_books':
            return globals()['ProcessBXBooksData']()
