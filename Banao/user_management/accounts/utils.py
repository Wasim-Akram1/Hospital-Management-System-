import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

def create_google_calendar_event(appointment):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)

    # Combine date and start_time to create a datetime object
    start_datetime = datetime.datetime.combine(appointment.date, appointment.start_time)
    end_datetime = start_datetime + datetime.timedelta(minutes=45)

    event = {
        'summary': f'Appointment with Dr. {appointment.doctor.user.profile.first_name} {appointment.doctor.user.profile.last_name}',
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event
