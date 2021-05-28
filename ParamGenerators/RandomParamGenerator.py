import random

from .ParamGenerator import ParamGenerator


class RandomParamGenerator(ParamGenerator):
    def set_source(self, source):
        # Nothing to do
        return True

    def get_param(self):
        return round(random.uniform(1, 10), 2)
