from dao.model.user_movie import UserMovie


class UserMovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user, movie):
        return self.session.query(UserMovie).filter(UserMovie.user == user, UserMovie.movie == movie).first()

    def create(self, user_movie):
        self.session.add(user_movie)
        self.session.commit()

        return user_movie

    def delete(self, user, movie):
        user_movie = self.get_one(user, movie)
        self.session.delete(user_movie)
        self.session.commit()
