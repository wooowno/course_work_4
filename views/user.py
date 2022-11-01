from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from container import user_service
from helpers.decorators import auth_required

user_ns = Namespace("user")


@user_ns.route("/")
class UserView(Resource):
    @auth_required
    def get(self):
        authorization = request.headers.get("Authorization")
        user = user_service.get_user(authorization)
        return UserSchema().dump(user), 200

    @auth_required
    def patch(self):
        req_json = request.json
        authorization = request.headers.get("Authorization")
        user_service.update_partial(data=req_json, authorization=authorization)
        return "", 204


@user_ns.route("/password")
class UserPasswordView(Resource):
    @auth_required
    def put(self):
        authorization = request.headers.get("Authorization")
        password = request.json.get("password")

        user_service.update_password(password=password, authorization=authorization)

        return "", 204
