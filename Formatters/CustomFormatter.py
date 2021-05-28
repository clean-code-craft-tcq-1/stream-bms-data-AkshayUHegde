from .Formatter import Formatter


class CustomFormatter(Formatter):
    def format(self, data):
        if not type(data) is dict:
            return "Format Error"
        output = ""
        for item in data:
            output += f"{item},{data[item]};"
        return output