from dao.model.genre import Genre
from helpers.constants import ENTITY_COUNT


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self, page):
        genres = self.session.query(Genre)

        if page is not None:
            page = int(page) - 1
            genres = genres.offset(ENTITY_COUNT * page).limit(ENTITY_COUNT)

        return genres.all()
