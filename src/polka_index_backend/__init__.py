from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/about')
    def about():
        return 'Polka Index Backend'

    return app