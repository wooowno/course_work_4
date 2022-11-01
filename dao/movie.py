from sqlalchemy import desc

from dao.model.movie import Movie
from helpers.constants import ENTITY_COUNT


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self, filters):
        movies = self.session.query(Movie)

        if "status" in filters and filters.get("status") == 'new':
            movies = movies.order_by(desc(Movie.year))

        if "page" in filters and filters.get("page") is not None:
            page = int(filters.get("page")) - 1
            movies = movies.offset(ENTITY_COUNT * page).limit(ENTITY_COUNT)

        return movies.all()
