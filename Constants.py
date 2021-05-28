from ParamGenerators import RandomParamGenerator, CSVParamGenerator
from Formatters import CustomFormatter, JSONFormatter
from OutputStreams import ConsoleOutputStream

PARAM_GENERATORS = {
    "random": RandomParamGenerator,
    "csv": CSVParamGenerator
}

FORMATTERS = {
    "json": JSONFormatter,
    "custom": CustomFormatter
}

OUTPUT_STREAMS = {
    "console": ConsoleOutputStream
}