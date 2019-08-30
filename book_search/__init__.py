from flask import Flask
app = Flask(__name__, static_folder='./web/dist', template_folder="./web/html")
from book_search.serve.serve import serve_blueprint
# register the blueprints
app.register_blueprint(serve_blueprint)
