from typing import Type
from sqlalchemy.exc import IntegrityError

from src.main.interface import RouterInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adpter(request: any, api_routes: Type[RouterInterface]) -> any:
    """
    Flask adapter
    :param request: any
    :param api_routes: Type[Route]
    :return: any
    """

    try:
        query_string_params = request.args.to_dict()

        if "pet_id" in query_string_params.keys():
            query_string_params["pet_id"] = int(query_string_params["pet_id"])

        if "user_id" in query_string_params.keys():
            query_string_params["user_id"] = int(query_string_params["user_id"])
    except IntegrityError:
        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    http_request = HttpRequest(header=request.headers, body=request.json, query=query_string_params)

    try:
        response = api_routes.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    return response
