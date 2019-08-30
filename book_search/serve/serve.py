# from search.word_cloud.word_cloud import WordClouds
from flask import render_template, Blueprint, request, jsonify


serve_blueprint = Blueprint('serve', __name__)
@serve_blueprint.route('/')
def index():
    return render_template("index.html", url="localhost", port="5000")


@serve_blueprint.route('/result', methods=['POST', 'GET'])
def index_post():
    text = request.args.get('book', None)
    return str(text).upper()
