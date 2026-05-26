import csv
from datetime import datetime
from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

params = {
    "api_key": SERPAPI_KEY,
    "engine": "google",
    "q": '("data analyst" OR "data analyst") (Delhi OR Noida OR Gurgaon) ("@gmail.com" OR "hr@" OR recruiter OR "send resume" OR "email cv")',
    "location": "Delhi, India",
    "gl": "in",
    "hl": "en",
    "num": 15,
}

def search_jobs():
    print("🔍 Searching for Data Analyst jobs WITH contact info...\n")
    
    search = GoogleSearch(params)
    results = search.get_dict()
    
    organic = results.get("organic_results", [])
    print(f"✅ Found {len(organic)} potential jobs with contact hints!\n")
    
    jobs_data = []
    
    for i, result in enumerate(organic, 1):
        job = {
            "title": result.get('title', 'N/A'),
            "link": result.get('link', 'N/A'),
            "snippet": result.get('snippet', ''),
            "source": result.get('source', 'N/A'),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        jobs_data.append(job)
        
        if i <= 10:
            print(f"{i}. {job['title']}")
            print(f"   🔗 {job['link']}")
            print(f"   📝 {job['snippet'][:160]}...\n")
    
    # Save to CSV
    with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link", "snippet", "source", "date"])
        writer.writeheader()
        writer.writerows(jobs_data)
    
    print(f"💾 Saved {len(jobs_data)} jobs to jobs.csv")

if __name__ == "__main__":
    search_jobs()