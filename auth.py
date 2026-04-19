from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']

def get_credentials():
    creds = None
    
    # Step 1: try to load existing token
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    # Step 2: if no valid creds, either refresh or do browser flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json',
                SCOPES)

            flow.run_local_server()
            creds = flow.credentials

        with open("token.json", "w") as f:
            f.write(creds.to_json())
        
            
    return creds