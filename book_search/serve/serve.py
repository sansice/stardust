# from search.word_cloud.word_cloud import WordClouds
from flask import render_template, Blueprint, request, jsonify
from book_search.process.churner.churn_data import ChurnData

serve_blueprint = Blueprint('serve', __name__)
@serve_blueprint.route('/')
def index():
    churn_data = ChurnData('bx_books')
    most_popular_items = churn_data.get_popular_items()
    return render_template("index.html", url="localhost", port="5000", items=most_popular_items)


@serve_blueprint.route('/process', methods=['POST', 'GET'])
def index_post():
    churn_data = ChurnData('bx_books')
    most_popular_items = churn_data.get_popular_items()
    # text = request.args.get('search_text', None)
    return str(most_popular_items)
