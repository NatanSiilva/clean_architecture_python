from typing import Type
from sqlalchemy.exc import IntegrityError

from src.main.interface import RouterInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adpter(request: any, api_routes: Type[Route]) -> any:
    """
    Flask adapter
    :param request: any
    :param api_routes: Type[Route]
    :return: any
    """

    http_request = HttpRequest(body=request.json)

    try:
        http_response = api_routes.route(http_request=http_request)
    except IntegrityError:
        https_error = HttpErrors.error_409()
        return HttpResponse(status_code=https_error["status_code"], body=https_error["body"])

    return http_response
