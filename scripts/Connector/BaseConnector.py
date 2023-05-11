from abc import ABC, abstractmethod

class BaseConnector():
    def __init__(self, client):
        self.client = client
        pass

    @abstractmethod
    def load_picture(self, picture_path: str):
        pass
    
    @abstractmethod
    def build_connector(self):
        pass