import os

import tomli
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

from scripts.Connector.BaseConnector import BaseConnector

CONFIG_PATH = '.config/.env'

class GDriveConnector(BaseConnector):
    def __init__(self):
        super().__init__()
        self.secret_file = "./.config/client_secrets.json"
        self.scopes = ['https://www.googleapis.com/auth/drive']
        self.build_connector()
        
    def load_picture(self, picture_path: str):
        #gets the drive parent directory id
        with open(CONFIG_PATH, mode = 'rb') as config_file:
            config = tomli.load(config_file)
            folder_id = config['GoogleDrive']['folder_id']

        #builds the file metadata and media
        file_metadata = {'name': os.path.basename(picture_path), 'parents': [folder_id]}
        media = MediaFileUpload(picture_path, mimetype='image/png', resumable=True)

        #loads the file to google drive
        file = self.drive.files().create(body=file_metadata, media_body=media, fields='id').execute()

        print(f'the file {picture_path} was successfully logged into the drive with ID: {file.get("id")}')
    
    def build_connector(self) -> None:
        credential_file = './.config/token.json'
        self.creds = None

        #Verify whether there is already a credential file
        if os.path.exists(credential_file):
            self.creds = Credentials.from_authorized_user_file(credential_file, self.scopes)

        #Save if it is necessary to build a new cred file from scratch
        if not self.creds or not self.creds.valid:
            
            #checks if it is possible to refresh the token
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            #gets a brand new credential secret
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.secret_file, self.scopes)
                breakpoint()
                self.creds = flow.run_local_server(port=0)
            #writes a new credential file
            with open(credential_file, 'w') as token:
                token.write(self.creds.to_json())
                
        self.drive = build('drive', 'v3', credentials=self.creds)