import os

import tomli
import boto3

from scripts.Connector.BaseConnector import BaseConnector

CONFIG_PATH = '.config/config.toml'

class S3Connector(BaseConnector):
    def __init__(self, client: str):
        super().__init__(client)
        self.build_connector()
        
    def load_picture(self, picture_path: str):
        obj_name = os.path.basename(picture_path)

        try:
            self.s3.upload_file(picture_path, self.destination_bucket, obj_name)
            breakpoint()
        except Exception as e:
            print(f'Error: {e}')

    def build_connector(self) -> None:
        self.destination_bucket = 'supin-'+self.client
        self.s3 = boto3.client('s3')
        breakpoint()