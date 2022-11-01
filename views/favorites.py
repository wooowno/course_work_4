from flask import request
from flask_restx import Resource, Namespace

from container import user_movie_service
from helpers.decorators import auth_required

favorite_ns = Namespace("favorites")


@favorite_ns.route("/movies/<int:mid>")
class FavoriteMovieView(Resource):
    @auth_required
    def post(self, mid):
        authorization = request.headers.get("Authorization")
        user_movie_service.create(authorization, mid)

        return "", 201

    @auth_required
    def delete(self, mid):
        authorization = request.headers.get("Authorization")
        user_movie_service.delete(authorization, mid)

        return "", 204
