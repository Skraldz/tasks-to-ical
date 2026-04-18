import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import credentials 
from google.auth.transport.requests import Requests

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']


def get_credentials():
    creds = None
    if os.path.exists("token.json") 
    

        # Step 1: try to load existing token
    if os.path.exists("token.json"):
        Credentials.from_authorized_user_file()
        pass
    
    # Step 2: if no valid creds, either refresh or do browser flow
    if not creds or not creds.valid:
        if # creds exist but are expired and have a refresh token:
            # refresh them
            pass
        else:
            # run browser flow and save result
            pass
        # Step 3: save the new/refreshed token to disk
    
    return creds