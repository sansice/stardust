import sys
import os
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from book_search import app


if __name__ == '__main__':

    app.config.from_object('configurations.DevelopmentConfig')
    app.run()
