import requests
from bs4 import BeautifulSoup
import re
import csv

# List of contact pages
contact_pages = [
    "https://example.com/contact", "https://recruiterpage.com/contact"
]

# Regex pattern to find emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# CSV file to store results
with open("recruiters_emails.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Agency Name", "Email", "Website"])

    for url in contact_pages:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract agency name from website title
            agency_name = soup.title.string.strip() if soup.title else "Unknown"

            # Find all emails
            emails = set(re.findall(email_pattern, soup.text))

            # Write to CSV
            for email in emails:
                writer.writerow([agency_name, email, url])

            print(f"Scraped {len(emails)} emails from {url}")

        except Exception as e:
            print(f"Error scraping {url}: {e}")

print("Scraping complete. Check 'recruiters_emails.csv'.")
