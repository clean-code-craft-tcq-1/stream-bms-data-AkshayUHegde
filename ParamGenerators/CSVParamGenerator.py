import csv

from .ParamGenerator import ParamGenerator


class CSVParamGenerator(ParamGenerator):
    def __init__(self):
        self.source = None
        self.count = 0

    def set_source(self, source):
        try:
            with open(source, newline='') as f:
                reader = csv.reader(f)
                self.source = list(reader)
            if self.source:
                return True
            else:
                return "Invalid Input"
        except:
            return "Invalid Input"

    def get_param(self):
        if len(self.source) == 0 or self.source[self.count % len(self.source)] is None:
            return "No Input"
        param = float(self.source[self.count % len(self.source)][0])
        self.count += 1
        return param
