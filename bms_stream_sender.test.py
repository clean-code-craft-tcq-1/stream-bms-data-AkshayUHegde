import unittest
import bms_stream_sender


class TypewiseTest(unittest.TestCase):
  def test_hello_world(self):
      self.assertEqual(bms_stream_sender.send_stream(), "Hello world")


if __name__ == '__main__':
  unittest.main()