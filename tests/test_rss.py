import json
import unittest
from unittest.mock import patch

from grabber.rss import RSSGrabber, RSSEntriesGrabber

REDDIT_RSS_ENDPOINT = 'https://www.reddit.com/r/news/.rss'
HABRAHABR_RSS_ENDPOINT = 'https://habrahabr.ru/rss/hubs/all/'

REDDIT_EXAMPLE_PATH = 'static_files/reddit.json'
HABRAHABR_EXAMPLE_PATH = 'static_files/habrahabr.json'


class RSSGrabberTest(unittest.TestCase):

    def load_rss_data(self, url):
        grabber = RSSGrabber(url=url)
        return grabber.load_data()

    def test_load_data(self):
        data = self.load_rss_data(url=REDDIT_RSS_ENDPOINT)
        self.assertTrue(isinstance(data, dict))

    def test_load_entries(self):
        grabber = RSSEntriesGrabber(url=REDDIT_RSS_ENDPOINT)
        entries = grabber.load_data()
        self.assertTrue(isinstance(entries, list))

    def test_load_data_without_request_external_service(self):
        with open(REDDIT_EXAMPLE_PATH) as json_file:
            reddit_dump_data = json.load(json_file)

        patched_request_igel = patch(
            target='grabber.rss.RSSGrabber.load_data',
            return_value=reddit_dump_data
        )
        with patched_request_igel:
            data = self.load_rss_data(url=REDDIT_RSS_ENDPOINT)
            self.assertEqual(data, reddit_dump_data)
