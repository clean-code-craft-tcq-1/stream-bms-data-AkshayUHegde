import json

from .Formatter import Formatter


class JSONFormatter(Formatter):
    def format(self, data):
        if not type(data) is dict:
            return "Format Error"
        return json.dumps(data)