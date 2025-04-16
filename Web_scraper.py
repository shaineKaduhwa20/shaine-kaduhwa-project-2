import requests
from bs4 import BeautifulSoup
import csv
import schedule
import time
from datetime import datetime

def scrape_jobs():
    print(f"\n⏰ Starting job scraping at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    url = 'https://vacancymail.co.zw/jobs/'
    print("📡 Sending request to the VacancyMail jobs page...")
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ Successfully fetched the page!")
        soup = BeautifulSoup(response.text, 'html.parser')

        print("🔍 Parsing job listings...")
        job_listings = soup.find_all('a', class_='job-listing')

        if not job_listings:
            print("⚠️ No job listings found. Check the structure or class names.")
            return

        filename = 'scraped_jobs.csv'
        print(f"📁 Creating CSV file: {filename}")
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Job Title', 'Company', 'Location', 'Expiry Date', 'Job Description'])

            print("✍️ Writing job listings to CSV...")
            for i, job in enumerate(job_listings[:10], start=1):
                try:
                    title_tag = job.find('h3', class_='job-listing-title')
                    title = title_tag.text.strip() if title_tag else "N/A"

                    company_tag = job.find('h4', class_='job-listing-company')
                    company = company_tag.text.strip() if company_tag else "N/A"

                    description_tag = job.find('p', class_='job-listing-text')
                    description = description_tag.text.strip() if description_tag else "N/A"

                    footer = job.find('div', class_='job-listing-footer')
                    footer_items = footer.find_all('li') if footer else []

                    location = footer_items[0].text.strip() if len(footer_items) > 0 else "N/A"
                    expiry = footer_items[1].text.replace("Expires", "").strip() if len(footer_items) > 1 else "N/A"

                    writer.writerow([title, company, location, expiry, description])
                    print(f"   ✅ Job #{i} written to file.")
                except Exception as e:
                    print(f"   ❌ Error writing job #{i}: {e}")

        print(f"🎉 Finished! CSV file '{filename}' has been updated.\n")

    else:
        print(f"❌ Failed to fetch the page. Status code: {response.status_code}")

# 🔁 Schedule the job
print("📅 Setting up schedule...")
schedule.every().day.at("09:15").do(scrape_jobs)

# 🚀 Run immediately for testing
scrape_jobs()

print("🕒 Job scheduler is running. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
