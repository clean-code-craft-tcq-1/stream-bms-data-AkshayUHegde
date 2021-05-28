from .OutputStream import OutputStream


class ConsoleOutputStream(OutputStream):
    def send(self, data):
        print(data)
        return True
