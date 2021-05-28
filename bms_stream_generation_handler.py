import threading
import time
import Constants


def format_output(formatter, data):
    return formatter.format(data)


def send_output(output_stream, data):
    return output_stream.send(data)


def create_param_map(param_generators):
    param_value_map = {}
    for param_name in param_generators:
        param_value_map[param_name] = param_generators[param_name].get_param()
    return param_value_map


def initialize_param_generators(param_generators, param_stream_sources):
    param_generators_status = {}
    for param_name in param_generators:
        param_generators_status[param_name] = param_generators[param_name].set_source(
            param_stream_sources[param_name]
        )
    return param_generators_status


def create_param_generators(param_stream_map):
    param_generators = {}
    for param_name in param_stream_map:
        param_generators[param_name] = Constants.PARAM_GENERATORS[param_stream_map[param_name]]()
    return param_generators


def send_stream_until_quit(param_generators, formatter, output_stream, frequency_per_s, quit_event, return_value):
    while not quit_event.is_set():
        param_value_map = create_param_map(param_generators)
        formatted_output = format_output(formatter, param_value_map)
        output_stream.send(formatted_output)
        wait_time_s = 1 / frequency_per_s
        time.sleep(wait_time_s)
        return_value.append("Running")
    return_value.append("Quit Received")


def start(param_stream_types, param_stream_sources, format_type, output_stream_type, frequency_per_s=1):
    param_generators = create_param_generators(param_stream_types)
    initialize_param_generators(param_generators, param_stream_sources)
    formatter = Constants.FORMATTERS[format_type]()
    output_stream = Constants.OUTPUT_STREAMS[output_stream_type]()
    quit_event = threading.Event()
    return_value = []
    send_loop = threading.Thread(target=send_stream_until_quit,
                                 args=(param_generators, formatter, output_stream, frequency_per_s, quit_event,
                                       return_value),
                                 daemon=True)
    send_loop.start()
    return quit_event, send_loop, return_value
