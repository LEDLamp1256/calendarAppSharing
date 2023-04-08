import os.path

import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
SCOPES = ['https://www.googleapis.com/auth/classroom.course-work.readonly', 'https://www.googleapis.com/auth/classroom.courses.readonly']
def classroomgetassignment(courseid):
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    try:
        service = build('classroom', 'v1', credentials=credentials, static_discovery = False)
        # print(service.courses().list().execute())
        course = service.courses().get(id=courseid).execute()
        print(f"Course found : {course.get('name')}")
        print(course)
        work = service.courses().courseWork().list(courseId=courseid).execute()
        print(work)
    except HttpError as error:
        print(f"An error occurred: {error}")
        print(f"Course not found: {courseid}")
        return error
    return work

def getclasses():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(Request())
            except google.auth.exceptions.RefreshError:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                credentials = flow.run_local_server(port=0)

        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    try:
        service = build('classroom', 'v1', credentials=credentials, static_discovery = False)
        courses = []
        page_token = None

        while True:
            # pylint: disable=maybe-no-member
            response = service.courses().list(pageToken=page_token, pageSize=100).execute()
            courses.extend(response.get('courses', []))
            page_token = response.get('nextPageToken', None)
            if not page_token:
                break

        if not courses:
            print("No courses found.")
            return
        print("Courses:")
        for course in courses:
            print(f"{course.get('name'), course.get('id')}")
        return courses
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

getclasses()
if __name__ == "__main__":
    classroomgetassignment(543949562448)