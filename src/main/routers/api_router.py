from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer, register_pet_composer, find_pet_composer, find_user_composer

from src.main.adapter import flask_adpter

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api", methods=["GET"])
def something():
    """This is a test route."""

    return jsonify({"message": "Server is up and running!"})


@api_routes_bp.route("/api/register/user", methods=["POST"])
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
