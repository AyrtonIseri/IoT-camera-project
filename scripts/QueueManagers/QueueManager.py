import os
import glob
import re

import tomli

from scripts.Connector.Connectors.S3Connector import S3Connector
from utils.Exceptions import FilenameNotFormattedException

CONFIG_PATH = "./.config/config.toml"

class Manager():
    def __init__(self, client: str, queue_path: str):
        self.queue_path = queue_path
        self.client = client
        self._get_connector()

    def process_queue(self):
        self._list_files()

        for file in self.queue:
            self.connector.load_picture(file, self.client)

            #logging to console
            filename = os.path.basename(file)
            print(f'Successfully loaded {filename} to remote storage')

        self._clean_buffer()

    def _get_connector(self):
        self.connector = S3Connector()

    def _list_files(self):
        self.queue = []

        for file in glob.glob(pathname=self.queue_path+'/*'):
            filename = os.path.basename(file)
            print(filename)
            file_valid = self._validate_file(filename=filename)

            if not file_valid:
                raise FilenameNotFormattedException(
                    f"""Filename must be formatted according to predetermined convention. 
                    Expected {self.pattern} but got {filename}"""
                )

            self.queue.append(file)

    def _validate_file(self, filename: str) -> bool:
        with open(CONFIG_PATH, 'rb') as config_file:
            config = tomli.load(config_file)
            self.pattern = config['Queue']['filename_pattern']

        validated = re.match(self.pattern, filename)

        if validated:
            return True
        else:
            return False

    def _clean_buffer(self):
        for file in glob.glob(pathname=self.queue_path+'/*'):
            self._assure_file_in_driver(file)
            os.remove(file)

    def _assure_file_in_driver(self, filename: str):
        pass