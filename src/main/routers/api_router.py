from flask import Blueprint, jsonify, request

from src.infra.repositories.user_repository import UserRepository
from src.data.find_user.find import FindUser
from src.main.composer import register_user_composer, register_pet_composer, find_pet_composer, find_user_composer
from src.main.adapter import flask_adpter
from src.main.auth_jwt import token_creator, token_verify

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api", methods=["GET"])
def something():
    """This is a test route."""

    return jsonify({"message": "Server is up and running!"})


@api_routes_bp.route("/api/register/user", methods=["POST"])
@token_verify
def register_user():
    """This is a route to register a user."""

    message = {}
    response = flask_adpter(request=request, api_routes=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
            },
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {
                "errors": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/register/pets", methods=["POST"])
@token_verify
def register_pets():
    """This is a route to register a user."""

    message = {}
    response = flask_adpter(request=request, api_routes=register_pet_composer())

    if response.status_code < 300:
        message = {
            "type": "pets",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {
                "type": "users",
                "id": response.body.user_id,
            },
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {
                "errors": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["GET"])
def finder_pets():
    """find pets route"""

    message = {}
    response = flask_adpter(request=request, api_routes=find_pet_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "pets",
                    "id": element.id,
                    "attributest": {
                        "name": element.name,
                        "specie": element.specie.value,
                        "age": element.age,
                    },
                    "relationships": {"owner": {"type": "users", "id": element.user_id}},
                }
            )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify({"error": {"status": response.status_code, "title": response.body["error"]}}),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["GET"])
def finder_users():
    """find users route"""

    message = {}
    response = flask_adpter(request=request, api_routes=find_user_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "users",
                    "id": element.id,
                    "attributest": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify({"error": {"status": response.status_code, "title": response.body["error"]}}),
        response.status_code,
    )


@api_routes_bp.route("/secret", methods=["GET"])
@token_verify
def secret_route():
    """This is a route to authorize a user."""

    return jsonify({"message": "You are authorized"}), 200


@api_routes_bp.route("/auth", methods=["POST"])
def authorization_route():
    """This is a route to authorize a user."""

    repository = UserRepository()
    find_user = FindUser(user_repository=repository)

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400

    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = find_user.by_name(name=username)

    if user["Data"] == []:
        return jsonify({"msg": "User not found"}), 404

    if user["Data"][0].password != password:
        return jsonify({"msg": "Bad password"}), 401

    data = []

    for element in user["Data"]:
        data.append(
            {
                "id": element.id,
                "name": element.name,
            }
        )

    token = token_creator.create_token(user_id=user["Data"][0].id)

    return jsonify({"token": token, "data": data}), 200
