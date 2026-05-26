import csv
import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def get_gmail_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)


def create_draft(service, to_email, subject, body, resume_path="resume.pdf"):
    """Create Gmail draft with resume attached"""
    message = MIMEMultipart()
    message['to'] = to_email
    message['subject'] = subject
    
    msg = MIMEText(body)
    message.attach(msg)
    
    # Attach resume
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(resume_path)}",
        )
        message.attach(part)
    
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    
    try:
        draft = service.users().drafts().create(userId="me", body={"message": {"raw": raw_message}}).execute()
        print(f"✅ Draft created successfully for: {to_email}")
        return draft
    except Exception as e:
        print(f"❌ Failed to create draft: {e}")
        return None


def main():
    print("📧 Creating Gmail Drafts...\n")
    
    try:
        with open("jobs_with_contacts.csv", "r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
    except FileNotFoundError:
        print("❌ jobs_with_contacts.csv not found!")
        return
    
    service = get_gmail_service()
    drafts_created = 0
    
    for job in reader:
        if job.get('emails'):
            from email_generator import generate_email
            email_data = generate_email(job)
            
            if email_data:
                draft = create_draft(
                    service=service,
                    to_email=email_data['to'],
                    subject=email_data['subject'],
                    body=email_data['body']
                )
                if draft:
                    drafts_created += 1
    
    print(f"\n🎯 Total Gmail drafts created: {drafts_created}")


if __name__ == "__main__":
    main()