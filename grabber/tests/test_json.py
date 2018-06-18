import json
import unittest

from grabber import JSONGrabber

SOME_JSON_FILE = 'grabber/static_files/reddit.json'


class JSONGrabberTest(unittest.TestCase):

    def test_load_data(self):
        grabber = JSONGrabber(path=SOME_JSON_FILE)
        real_data = grabber.load_data()

        with open(SOME_JSON_FILE) as json_file:
            expected_data = json.load(json_file)

        self.assertEqual(real_data, expected_data)
