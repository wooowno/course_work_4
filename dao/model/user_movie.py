from marshmallow import Schema, fields

from setup_db import db


class UserMovie(db.Model):
    __tablename__ = 'user_movie'
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    user = db.relationship("User")

    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    movie = db.relationship("Movie")


class UserMovieSchema(Schema):
    user_id = fields.Int()
    movie_id = fields.Int()
