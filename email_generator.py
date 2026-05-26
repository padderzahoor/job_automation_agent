import csv
from dotenv import load_dotenv
import os

load_dotenv()

def generate_email(job, your_name="Padder Zahoor"):
    """Generate a professional, tailored email"""
    
    company = job.get('company', job.get('source', 'the company'))
    title = job.get('title', 'Data Analyst position')
    emails = job.get('emails', '')
    
    if not emails:
        return None
    
    recruiter_email = emails.split(',')[0].strip()
    
    email_body = f"""Hi,

I came across the {title} opportunity at {company} and was very interested.

I have hands-on experience with SQL, Python, Excel, Power BI, and data analysis projects. I am particularly strong in turning raw data into actionable insights.

I have attached my resume for your review. I would love the opportunity to discuss how my skills can add value to your team.

Looking forward to hearing from you.

Best regards,
{your_name}
Data Analyst
"""

    subject = f"Application for {title} at {company}"

    return {
        "to": recruiter_email,
        "subject": subject,
        "body": email_body,
        "job_title": title,
        "company": company
    }


def main():
    print("✉️  Generating Tailored Emails...\n")
    
    try:
        with open("jobs_with_contacts.csv", "r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
    except FileNotFoundError:
        print("❌ jobs_with_contacts.csv not found! Run extract_contacts.py first.")
        return
    
    emails_generated = 0
    
    for job in reader:
        if job.get('emails'):
            email_data = generate_email(job)
            if email_data:
                print(f"✅ Draft ready for: {job.get('title')}")
                print(f"   To: {email_data['to']}")
                print(f"   Subject: {email_data['subject']}\n")
                emails_generated += 1
    
    print(f"\n🎯 Total email drafts generated: {emails_generated}")

if __name__ == "__main__":
    main()