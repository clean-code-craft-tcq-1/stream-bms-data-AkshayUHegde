import io
import time
import unittest.mock
import bms_stream_generation_handler
from OutputStreams import ConsoleOutputStream
from ParamGenerators import CSVParamGenerator
from Formatters import JSONFormatter, CustomFormatter


class BMSStreamSenderTest(unittest.TestCase):
    def test_invalid_input(self):
        test_param_generators = {"test1": CSVParamGenerator()}
        test_param_stream_sources = {"test1": "sources\\invalid_csv.csv"}
        test_output = bms_stream_generation_handler.initialize_param_generators(test_param_generators, test_param_stream_sources)
        self.assertEqual(test_output, {'test1': 'Invalid Input'})

    def test_no_input(self):
        test_param_generators = {"test2": CSVParamGenerator()}
        test_param_stream_sources = {"test2": "sources\\no_input.csv"}
        bms_stream_generation_handler.initialize_param_generators(test_param_generators, test_param_stream_sources)
        test_output = bms_stream_generation_handler.create_param_map(test_param_generators)
        self.assertEqual(test_output, {"test2": "No Input"})

    def test_format_error(self):
        test_formatters = [JSONFormatter(), CustomFormatter()]
        invalid_input = ["param1", 1.5, "param2", 3]
        for test_formatter in test_formatters:
            test_output = bms_stream_generation_handler.format_output(test_formatter, invalid_input)
            self.assertEqual(test_output, 'Format Error')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_send_output_console(self, mock_stdout):
        test_output_stream = ConsoleOutputStream()
        test_input = "TestParamValue"
        bms_stream_generation_handler.send_output(test_output_stream, test_input)
        self.assertEqual(mock_stdout.getvalue().strip(), test_input)

    def test_quit_thread(self):
        test_param_stream_types = {"charge_rate": "random", "temp_in_c": "csv"}
        test_param_stream_sources = {"charge_rate": None, "temp_in_c": "sources\\battery_temps.csv"}
        test_format_type = "json"
        test_output_stream_type = "console"
        quit_event_control, bms_stream_loop, return_value = bms_stream_generation_handler.start(test_param_stream_types,
                                                                                                test_param_stream_sources,
                                                                                                test_format_type,
                                                                                                test_output_stream_type)
        time.sleep(1)
        quit_event_control.set()
        bms_stream_loop.join()
        self.assertEqual(return_value[-1], "Quit Received")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_send_loop_custom_formatting_console_output(self, mock_stdout):
        test_param_stream_types = {"temp_in_c": "csv"}
        test_param_stream_sources = {"temp_in_c": "sources\\battery_temps.csv"}
        test_format_type = "custom"
        test_output_stream_type = "console"
        test_frequency = 1
        quit_event_control, bms_stream_loop, _ = bms_stream_generation_handler.start(test_param_stream_types,
                                                                                     test_param_stream_sources,
                                                                                     test_format_type,
                                                                                     test_output_stream_type)
        time.sleep(2/test_frequency)
        quit_event_control.set()
        bms_stream_loop.join()
        self.assertEqual(mock_stdout.getvalue().strip(), "temp_in_c,5.26;\ntemp_in_c,75.76;")

unittest.main()
