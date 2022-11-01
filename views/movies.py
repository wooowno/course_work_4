from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from container import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page,
        }
        movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(movies)
        return result, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        result = MovieSchema().dump(movie)
        return result, 200
