import csv
import re
import requests
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv

load_dotenv()

def clean_text(text):
    # Replace common junk patterns
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(?i)opt-out|unsubscribe|click here|download', ' ', text)
    return text

def extract_emails_and_phones(text):
    text = clean_text(text)
    
    # Strong email regex
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    
    # Filter bad emails
    bad_keywords = ['opt-out', 'unsubscribe', 'example', 'domain', 'test', 'noreply', 'no-reply']
    valid_emails = [e.lower() for e in emails if not any(bad in e.lower() for bad in bad_keywords)]
    
    # Phone regex (India)
    phone_pattern = r'\b(?:\+91|0)?[6-9]\d{9}\b'
    phones = re.findall(phone_pattern, text)
    
    return list(set(valid_emails)), list(set(phones))

def extract_contacts_from_url(url):
    if not url or url == "N/A":
        return [], []
    
    print(f"🌐 Visiting: {url[:80]}...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=12)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=" ", strip=True)
        
        emails, phones = extract_emails_and_phones(text)
        
        return emails, phones
        
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return [], []

def main():
    print("📧 Starting Improved Regex Contact Extraction...\n")
    
    try:
        with open("jobs.csv", "r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
    except FileNotFoundError:
        print("❌ jobs.csv not found!")
        return
    
    enriched_jobs = []
    
    for i, job in enumerate(reader[:10], 1):
        print(f"\n{i}. {job.get('title', 'N/A')}")
        
        emails, phones = extract_contacts_from_url(job.get('link'))
        
        enriched_job = {
            'title': job.get('title', ''),
            'link': job.get('link', ''),
            'snippet': job.get('snippet', ''),
            'source': job.get('source', ''),
            'date': job.get('date', ''),
            'emails': ", ".join(emails) if emails else "",
            'phones': ", ".join(phones) if phones else "",
            'status': "Processed"
        }
        
        enriched_jobs.append(enriched_job)
        
        if emails:
            print(f"   ✅ Found Emails: {enriched_job['emails']}")
        if phones:
            print(f"   📱 Found Phones: {enriched_job['phones']}")
        
        time.sleep(2.5)
    
    # Save
    fieldnames = ['title', 'link', 'snippet', 'source', 'date', 'emails', 'phones', 'status']
    with open("jobs_with_contacts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_jobs)
    
    print(f"\n✅ Extraction complete!")
    print(f"Total emails found: {sum(1 for job in enriched_jobs if job.get('emails'))}")

if __name__ == "__main__":
    main()