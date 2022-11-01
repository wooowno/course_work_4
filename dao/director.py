from dao.model.director import Director
from helpers.constants import ENTITY_COUNT


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self, page):
        directors = self.session.query(Director)

        if page is not None:
            page = int(page) - 1
            directors = directors.offset(ENTITY_COUNT * page).limit(ENTITY_COUNT)

        return directors.all()
