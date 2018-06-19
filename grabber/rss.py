import feedparser

from .abstract_classes import Grabber


class RSSGrabber(Grabber):
    url: str

    def __init__(self, url: str):
        self.url = url

    def load_data(self) -> dict:
        return feedparser.parse(self.url)


class RSSEntriesGrabber(RSSGrabber):

    def load_data(self) -> list:
        return super().load_data()['entries']
