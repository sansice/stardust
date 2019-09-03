# home_dir = "D:\sans\OneDrive - HCL Technologies Ltd\work\HCL\projects\stardust"
import os

project_name = 'stardust'
sub_project = 'book_search'
file_path = os.path.dirname(os.path.abspath(__file__))
sub_project_home = os.path.dirname(os.path.dirname(file_path))
project_home = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
data_path = os.path.join(sub_project_home, 'data')
work_dir = os.path.join(sub_project_home, 'work_dir')

# bx_books_data_files -
bx_books_csv_path = os.path.join(data_path, 'bxbooks')
bx_books_info_csv = os.path.join(bx_books_csv_path, 'BX-Books.csv')
bx_books_users_csv = os.path.join(bx_books_csv_path, 'BX-Users.csv')
bx_books_ratings_csv = os.path.join(bx_books_csv_path, 'BX-Book-Ratings.csv')
bx_books_encoding = 'latin-1'
bx_books_algorithm = 'brute'
bx_books_metrics = 'cosine'

