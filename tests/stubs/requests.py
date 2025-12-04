class RequestException(Exception):
    """Base exception for requests module"""
    pass


class Response:
    def __init__(self):
        self.text = ""

    def raise_for_status(self):
        pass


def get(url, **kwargs):
    return Response()
