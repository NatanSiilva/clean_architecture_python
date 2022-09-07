from datetime import datetime, timedelta
import time
import jwt


class TokenCreator:
    """This class is used to create a token."""

    def __init__(self, token_key: str, exp_time_min: int, refresh_time_min: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time_min

    def create_token(self, user_id: int) -> str:
        """
        This method create a token
        :param user_id: int
        :return: token
        """
        return self.__encode_token(user_id=user_id)

    def refresh_token(self, token: str) -> str:
        """
        This method refresh a token
        :param token: str
        :return: token
        """

        token_information = jwt.decode(token, key=self.__TOKEN_KEY, algorithms="HS256")

        token_uid = token_information["user_id"]
        expires = token_information["exp"]

        if ((expires - time.time()) / 60) < self.__REFRESH_TIME_MIN:
            return self.__encode_token(user_id=token_uid)

        return token

    def __encode_token(self, user_id: int) -> str:
        """
        This method encode a token
        :param user_id: int
        :return: token
        """

        expires = datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN)
        token = jwt.encode({"exp": expires, "user_id": user_id}, key=self.__TOKEN_KEY, algorithm="HS256")

        return token
