import csv
import json

from .abstract_classes import Grabber


# noinspection PyAbstractClass
class FileGrabber(Grabber):
    path: str

    def __init__(self, path: str):
        self.path = path


class CSVGrabber(FileGrabber):

    def load_data(self) -> list:
        with open(self.path) as csv_file:
            return list(csv.reader(csv_file))


class JSONGrabber(FileGrabber):

    def load_data(self) -> dict:
        with open(self.path) as json_file:
            return json.load(json_file)
