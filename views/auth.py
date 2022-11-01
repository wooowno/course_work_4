from flask import request
from flask_restx import Namespace, Resource

from container import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class RegisterView(Resource):
    def post(self):
        req_json = request.json

        email = req_json.get("email")
        password = req_json.get("password")

        auth_service.create_user(data={"email": email, "password": password})

        return "", 201


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        req_json = request.json

        email = req_json.get("email")
        password = req_json.get("password")

        if None in [email, password]:
            return "", 400

        tokens = auth_service.generate_token(email=email, password=password)

        return tokens, 201

    def put(self):
        data = request.json

        token = data.get("refresh_token")

        if token is None:
            return "", 400

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
