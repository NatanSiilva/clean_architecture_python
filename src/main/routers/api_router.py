from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer

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
            "Type": "users",
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
