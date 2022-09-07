from src.main.configs.jwt_config_file import jwt_config
from .token_creator import TokenCreator

token_creator = TokenCreator(
    token_key=jwt_config["TOKEN_KEY"],
    exp_time_min=jwt_config["EXP_TIME_MIN"],
    refresh_time_min=jwt_config["REFRESH_TIME_MIN"],
)
