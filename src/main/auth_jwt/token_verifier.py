from functools import wraps
from flask import jsonify, request
import jwt

from src.main.configs.jwt_config_file import jwt_config

# from .token_handle import token_creator


def token_verify(function: callable) -> callable:
    """This function is used to verify a token."""

    @wraps(function)
    def decorated(*args, **kwargs):
        """This function is used to verify a token."""

        raw_token = request.headers.get("Authorization")
        uid = request.headers.get("uid")

        if not raw_token or not uid:
            return jsonify({"msg": "Missing token or uid"}), 401

        try:
            token = raw_token.split()[1]
            token_information = jwt.decode(token, key=jwt_config["TOKEN_KEY"], algorithms="HS256")
            token_uid = token_information["user_id"]

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token is invalid"}), 401
        except KeyError as error:
            return jsonify({"error": f"Token is invalid {error}"}), 401

        if int(token_uid) != int(uid):
            return jsonify({"error": "User not authorized"}), 401

        # next_token = token_creator.refresh_token(token=token)

        return function(*args, **kwargs)

    return decorated
