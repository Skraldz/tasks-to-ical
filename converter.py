from googleapiclient.discovery import build
from ics import Calendar, Event

def get_tasks_as_ical(creds):
    service = build('tasks', 'v1', credentials=creds)
    calendar = Calendar()

    # fetch all task lists
    tasklists = service.tasklists().list().execute()
    
    for tasklist in tasklists.get('items', []):
        list_id = tasklist['id']
        
        # fetch tasks for this list
        tasks = service.tasks().list(tasklist=list_id).execute()
        
        for task in tasks.get('items', []):
            if task.get('due'):  # only tasks with a due date
                event = Event()
                event.name = task["title"]
                event.begin = task['due']
                # set event.name and event.begin
                calendar.events.add(event)

    return calendar.serialize()       

