import sys
import time
import argparse

import bms_stream_generation_handler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Runs the sender mechanism for the TCQ project. See -h for more'
                                                 'information')
    parser.add_argument("-p", "--params", help="Comma separated list of params. Ex: -p param1,param2",
                        type=str, default="charge_rate,temp_in_c")
    parser.add_argument("-s", "--stream_types", help="Comma separated list of stream types in the same"
                        "order as params. Each stream type can be either random or csv. Ex: -s random,csv", type=str,
                        default="random,csv")
    parser.add_argument("-ss", "--stream_sources", help="Comma separated list of stream sources in the same"
                        "order as params. None for random and specify csv file path for csv. Ex: -ss None,params.csv",
                        type=str, default="None,sources\\battery_temps.csv")
    parser.add_argument("-o", "--output_format", help="Output stream format. Choose json or custom. Customer stream"
                        "format is printed as param1,param1Value;param2,param2Value;\n and so on. Ex: -o json",
                        type=str, default="json", choices=["json", "custom"])
    parser.add_argument("-f", "--frequency", help="Frequency of the output in per second. Ex: -f 1", type=int,
                        default=1)

    args = parser.parse_args()
    param_names = args.params.split(',')
    param_sources = args.stream_sources.split(',')
    param_types = args.stream_types.split(',')
    param_stream_types = {}
    param_stream_sources = {}
    for index, param_name in enumerate(param_names):
        param_stream_types[param_name] = param_types[index]
        param_stream_sources[param_name] = param_sources[index]
    output_format_type = args.output_format
    output_frequency = args.frequency
    # Currently supports only console per requirements
    output_stream_type = "console"

    # Use Ctrl+C to exit
    quit_event, send_loop, return_value = bms_stream_generation_handler.start(
        param_stream_types,
        param_stream_sources,
        output_format_type,
        output_stream_type,
        output_frequency
    )
    try:
        while True:
            time.sleep(1 / output_frequency)
    except KeyboardInterrupt:
        quit_event.set()
        send_loop.join()