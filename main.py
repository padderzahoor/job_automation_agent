from dotenv import load_dotenv
import time
import os

load_dotenv()

def run_full_cycle():
    print("="*70)
    print("🚀 FULL JOB AUTOMATION SYSTEM")
    print("="*70)
    
    # Step 1: Search Jobs
    print("\n[1/4] 🔍 Searching for new Data Analyst jobs...")
    from search_jobs import search_jobs
    search_jobs()
    
    print("\n" + "-"*60)
    
    # Step 2: Extract Contacts
    print("\n[2/4] 📧 Extracting recruiter emails & phones...")
    from extract_contacts import main as extract_contacts
    extract_contacts()
    
    print("\n" + "-"*60)
    
    # Step 3: Generate Tailored Emails
    print("\n[3/4] ✉️  Generating personalized emails...")
    from email_generator import main as generate_emails
    generate_emails()
    
    print("\n" + "-"*60)
    
    # Step 4: Create Gmail Drafts
    print("\n[4/4] 📝 Creating Gmail Drafts with Resume...")
    from gmail_drafts import main as create_drafts
    create_drafts()
    
    print("\n" + "="*70)
    print("✅ FULL CYCLE COMPLETED SUCCESSFULLY!")
    print("You can now review the drafts in Gmail.")
    print("Run again anytime with: python main.py")
    print("="*70)

if __name__ == "__main__":
    run_full_cycle()