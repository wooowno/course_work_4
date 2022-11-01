import hashlib

import jwt

from dao.model.user import User
from dao.user import UserDAO
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGORITHM


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_user(self, authorization):
        access_token = authorization.split("Bearer ")[-1]
        data = jwt.decode(access_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data.get("email")
        return self.get_by_email(email)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        user = User(**data)

        user.password = self.get_hash(user.password)

        return self.dao.create(user)

    def update_password(self, password, authorization):
        user = self.get_user(authorization)

        user.password = self.get_hash(password)

        return self.dao.update(user)

    def update_partial(self, data, authorization):
        user = self.get_user(authorization)

        if "email" in data:
            user.email = data["email"]
        if "password" in data:
            user.password = self.get_hash(data["password"])
        if "name" in data:
            user.name = data["name"]
        if "surname" in data:
            user.surname = data["surname"]
        if "favorite_genre" in data:
            user.favorite_genre = data["favorite_genre"]

        return self.dao.update(user)

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def compare_passwords(self, hash_password, other_password):
        other_hash = self.get_hash(other_password)
        return hash_password == other_hash
