class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error_422():
        """Method to define error 422"""

        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        """Method to define error 400"""

        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_409():
        """Method to define error 409"""

        return {"status_code": 409, "body": {"error": "Conflict"}}
