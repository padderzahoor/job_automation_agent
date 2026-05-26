# Job Automation System 🚀

An intelligent, automated job application system that searches for Data Analyst roles, extracts recruiter contacts, generates tailored emails, and creates Gmail drafts with your resume attached.

---
![Agent in Action](screenshots/screenshot_1.png)

## 📍 Problem Statement

Searching and applying for jobs is an extremely **tedious and time-consuming** process. 

Manually applying to 10–20 jobs every day — searching on different portals, finding recruiter emails, tailoring resumes and cover letters — was a **daily headache**. 

I built this system to **automate the repetitive part** of job hunting while keeping full control and human touch in the final step (reviewing & sending emails).

---

## ✨ Features

- **Automated Job Search** — Finds Data Analyst roles in Delhi-NCR
- **Smart Contact Extraction** — Pulls recruiter emails from job pages
- **Personalized Email Generation** — Creates professional, tailored application emails
- **Gmail Draft Creation** — Automatically creates drafts with resume attached
- **Safe & Controlled** — You review drafts before sending (avoids spam)

---

## 🛠️ Tech Stack

- Python 3
- SerpAPI (Google Search)
- BeautifulSoup + Requests
- Gmail API
- OpenAI (optional for better extraction)
- CSV-based storage

---

## 📁 Project Structure
job-automation/
├── main.py                    # Runs full pipeline
├── search_jobs.py             # Job searching
├── extract_contacts.py        # Contact extraction
├── email_generator.py         # Email writing
├── gmail_drafts.py            # Gmail draft creation
├── resume.pdf                 # Your resume
├── .env                       # API keys
├── credentials.json           # Google OAuth
├── jobs.csv                   # Extracted data
├── jobs_with_contacts.csv     # Extracted emails and phone numbers
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md 

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd job-automation

2. **Setup EnvironmentBash**
    python -m venv venv
    venv\Scripts\activate        # Windows
    pip install -r requirements.txt
    playwright install

3. **Add API Keys**
    Add SERPAPI_KEY in .env
    Add OPENAI_API_KEY (optional)

4. **Google Gmail API Setup**
    Enable Gmail API in Google Cloud Console
    Download credentials.json and place in project root

5. **Run the SystemBash**
    python main.py

---

## ⚠️ Important Notes

- Creates **drafts only** — you manually review and send
- Designed to be safe and human-like
- Customize search queries as needed

---
## 📋 Next Improvements (Roadmap)

Smart job filtering (experience level, tech stack)
AI-powered email personalization using job description
Auto-send only 1 high-confidence email per cycle
Scheduler (run every 6 hours)
Dashboard / Logging

---

## 👤 Author

**Padder Zahoor**

⭐ Show Your Support
If this project helped you, please give it a star ⭐