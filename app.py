from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.favorites import favorite_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.user import user_ns

app = Flask(__name__)
app.config.from_object(Config())
app.config.from_envvar("APP_SETTINGS", silent=True)

db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)
api = Api(app)

api.add_namespace(director_ns)
api.add_namespace(genre_ns)
api.add_namespace(movie_ns)
api.add_namespace(user_ns)
api.add_namespace(auth_ns)
api.add_namespace(favorite_ns)

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
