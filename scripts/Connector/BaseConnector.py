from abc import ABC, abstractmethod

class BaseConnector():
    def __init__(self):
        pass

    @abstractmethod
    def load_picture(self, picture_path: str, client: str):
        pass
    
    @abstractmethod
    def build_connector(self):
        pass