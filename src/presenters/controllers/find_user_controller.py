from typing import Type

from src.domain.use_cases import FindUser
from src.main.interface.router import RouterInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindUserController(RouterInterface):
    """Class to define controller to find_user use case"""

    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Method to call use case
        param http_request: Instance of HttpRequest
        return: Instance of HttpResponse
        """

        response = None

        if http_request and http_request.query:
            query_str_params = http_request.query.keys()

            if "user_id" in query_str_params and "user_name" in query_str_params:
                user_id = http_request.query["user_id"]
                user_name = http_request.query["user_name"]

                response = self.find_user_use_case.by_id_and_name(user_id=user_id, name=user_name)

            elif "user_id" in query_str_params and "user_name" not in query_str_params:
                user_id = http_request.query["user_id"]

                response = self.find_user_use_case.by_id(user_id=user_id)

            elif "user_id" not in query_str_params and "user_name" in query_str_params:
                user_name = http_request.query["user_name"]

                response = self.find_user_use_case.by_name(name=user_name)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
