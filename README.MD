# 📄 VacancyMail Jobs Scraper

A scheduled Python web scraper that pulls job listings from [VacancyMail.co.zw](https://vacancymail.co.zw/jobs/) and stores them in a CSV file.

---

## 📚 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [Setup](#setup)  
5. [Usage](#usage)  
6. [Output](#output)  
7. [Error Handling](#error-handling)  
8. [Contributing](#contributing)  
9. [License](#license)  

---

## 🔍 Overview

This script scrapes job titles, companies, locations, expiry dates, and descriptions, saving them to `scraped_jobs.csv`. It runs daily at **09:15 AM** and logs progress in the terminal.

---

## ✨ Features

- 🕘 Daily scheduled scraping  
- 📂 CSV file auto-creation & updating  
- 💬 Console logging with emoji feedback  
- 🛡️ Built-in error handling  
- 🔍 Pulls detailed job info (up to 10 listings per run)

---

## 🧰 Requirements

- Python 3.6+
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `schedule`
  - `csv` and `datetime` (built-in)

Install with:

```bash
pip install requests beautifulsoup4 schedule
⚙️ Setup
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/vacancymail-jobs-scraper.git
cd vacancymail-jobs-scraper
Install dependencies (optional: add a requirements.txt):

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Run the script:

bash
Copy
Edit
python scraper.py
Executes immediately for testing

Schedules future runs daily at 09:15 AM

Keep the terminal open or run via a background service (e.g., cron or Task Scheduler)

📁 Output
Data is saved to scraped_jobs.csv with:


Column	Description
Job Title	Position title
Company	Employer
Location	City/region
Expiry Date	Application deadline
Job Description	Summary of job listing
⚠️ Error Handling
Graceful handling of missing tags (defaults to "N/A")

Skips over broken items without stopping the script

Checks HTTP status codes before parsing

🤝 Contributing
Contributions welcome! To contribute:

Fork the repo

Create a new branch

Make changes & test

Open a pull request

📄 License
MIT License © 2025 Shaine Kaduhwa