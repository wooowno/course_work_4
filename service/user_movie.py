from dao.model.user_movie import UserMovie
from dao.user_movie import UserMovieDAO
from service.movie import MovieService
from service.user import UserService


class UserMovieService:
    def __init__(self, dao: UserMovieDAO, user_service: UserService, movie_service: MovieService):
        self.dao = dao
        self.user_service = user_service
        self.movie_service = movie_service

    def create(self, authorization, mid):
        user = self.user_service.get_user(authorization)
        movie = self.movie_service.get_one(mid)

        user_movie = UserMovie(user=user, movie=movie)

        return self.dao.create(user_movie)

    def delete(self, authorization, mid):
        user = self.user_service.get_user(authorization)
        movie = self.movie_service.get_one(mid)

        self.dao.delete(user, movie)
