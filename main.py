from fastapi import FastAPI, Response
from auth import get_credentials
from converter import get_tasks_as_ical

app = FastAPI()

@app.get("/")
def root():
    return{"status": "ok"}

@app.get("/tasks.ics")
def get_google_tasks():
    creds = get_credentials()
    response = get_tasks_as_ical(creds)
    return Response(content=response, media_type="text/calendar")
    