import requests
from bs4 import BeautifulSoup
import re
import csv

# List of contact pages
contact_pages = [
    "https://buildrec.com/contact/",
"https://www.roberthalf.com/",
"https://www.eurolondon.com/",
"https://www.evenbreak.co.uk/",
"https://tiger-recruitment.com/about-us/contact/",
"https://www.reed.com/candidates/get-in-touch",
"https://www.jac-recruitment.co.uk/about-us/work-with-us",
"https://www.frontrecruitment.co.uk/contact/",
"https://hire-ground.co.uk/contact/",
"https://euro-recruitment.co.uk/contact-us/",
"https://rulerecruitment.com/",
"https://www.eligo.co.uk/contact-us/",
"https://www.focalpointrecruitment.co.uk/contact",
"https://www.thconsultants.co.uk/contact",
"https://evolvewithinrecruitment.com/contact-us",
"https://www.soarrecruitment.co.uk/contact",
"https://www.berryrecruitment.co.uk/contact-berry",
"https://www.therecruitmentshop.co.uk/",
"https://www.pin-point.co.uk/contact-3",
"https://www.kennethbrian.co.uk/",
"https://www.lloydrecruitment.co.uk/",
"https://www.worthrecruiting.me/cm/contact-us",
"https://www.teamoneuk.com/",
"https://e-personnelrecruitment.co.uk/contact/",
"https://www.optimarecruitment.co.uk/",
"https://www.tate.co.uk/contact-us/",
"https://www.rockpoolrecruitment.co.uk/contact-us",
"https://www.specialist-recruit.co.uk/",
"https://www.jaderecruitment.net/",
"https://www.youpersonnel.co.uk/contact-us",
"https://www.strong-group.co.uk/",
"https://www.cbsbutler.com/cm/contact-us",
"https://yourrecruitgroup.com/",
"https://harris-global.com/contact",
"https://julieroserecruitment.co.uk/contact.html",
"https://crosswaysrecruitment.co.uk/contact-us/",
"https://www.temptingrecruitment.co.uk/contact",
"https://www.impactnationwiderecruitment.co.uk/contact/",
"https://www.laykarecruitment.com/contact/",
"https://otrsales.co.uk/contact",
"https://lindahillrecruitment.co.uk/contact-us/",
"https://www.unity-recruitment.co.uk/contact-us",
"https://responserecruitment.co.uk/",
"https://londonjobs.london/contact.php",
"https://www.sheridanward.co.uk/",
"https://aesn.co.uk/contact-us/",
"https://www.knightsbridgerecruitment.com/contact-us/",
"https://www.rmsrecruitment.com/contact-us/",
"https://www.loverecruitmentgroup.com/",
"https://www.spotlightrecruitment.com/contact-us/",
"https://platform-recruitment.com/contact-us",
"https://www.ashbyjenkinsrecruitment.co.uk/",
"https://www.tpp.co.uk/contact-us/",
"https://www.investigo.co.uk/contact-us",
"https://www.upgraderecruitment.co.uk/",
"https://www.ontrakrecruitment.co.uk/contact-us",
"https://fivepoint.co.uk/",
"https://www.evorecruit.co.uk/contact",
"https://dingorecruitment.com/contact/",
"https://www.yellowcat.london/contact-us/",
"https://www.netos.co.uk/contact",
"https://www.getrecruited.io/say-hi",
"https://www.thehingroup.com/contact/",
"https://www.ruby-group.com/contact-us",
"https://www.risetechnical.co.uk/contact-us?source=google.com",
"https://www.planbrecruitment.co.uk/",
"https://www.time2shinerecruitment.com/apply",
"https://www.4leisurerecruitment.co.uk/contact/",
"https://skilledhealthcarerecruitment.co.uk/contact-us/",
"https://ortusrecruitment.com/contact/",
"https://www.corr-recruitment.co.uk/contact/",
"https://www.dobetterrecruitmentandstaffing.com/contact-us",
"https://roiresources.co.uk/contact/",
"https://www.vibeteaching.co.uk/connect/",
"https://www.harrisonsrecruitment.com/contact-us",
"https://www.daleyrecruitment.com/contact-us/",
"https://www.extrastaff.com/branch-network?location=Head+Office&postcode=",
"https://www.constructrecruitment.com/",
"https://www.capstone-recruitment.com/contact-us",
"https://www.park-avenue.co.uk/get-in-touch",
"https://www.people-first.co.uk/contact",
"https://carnegieconsulting.co.uk/contact-us/",
"https://www.signaturerecruitment.co.uk/",
"https://austindean.co.uk/",
"https://www.pearrecruitment.com/systempages/contact-us",
"https://fortusrec.co.uk/contact/",
"https://publicsectorrecruitment.co.uk/Contact",
"https://www.bblproperty.co.uk/contact-us/",
"https://www.mosaic-recruitment.com/",
"https://stormx.co.uk/contact",
"https://www.blackpointrecruitment.co.uk/",
"https://madisons.org.uk/",
"https://www.jdsrecruitment.co.uk/contact-us/",
"https://ignite-recruitment.co.uk/",
"https://www.berryrecruitment.co.uk/contact-berry",
"https://romans-rg.com/",
"https://www.prs.uk.com/",
"https://www.the-destiny.co.uk/contact.php",
"https://www.fsr.uk.com/contact-us/",
"https://www.major-recruitment.com/",
"https://www.andersonrecruitment.co.uk/contact",
"https://www.frame-recruitment.com/",
"https://www.alliance-recruitment.com/contact",
"https://www.elevationrecruitmentgroup.com/contact-us",
"https://www.acceptrec.co.uk/contact-us",
"https://www.amjrecruitment.co.uk/contact-us/",
"https://www.fixedfeeplacements.co.uk/contact",
"https://twentyfourgroup.co.uk/contact/",
"https://www.larecruitment.net/",
"https://www.worldteachers.net/contact-us.aspx",
"https://www.connectrecruit.ie/contact",
"https://arconrecruitment.com/contact-us/",
"https://therecruitmentco.uk/contact/",
"https://recruitmentpartnershipireland.co.uk/contact/",
"https://nwesrecruitment.co.uk/",
"https://www.psiglobalrecruitment.com/contact/",
"https://www.deluxe-recruitment.co.uk/contact",
"https://dcsrecruitment.com/contact-us/",
"https://imperialrecruitmentgroup.com/contact/",
"https://www.citrus-connect.co.uk/contact-us/",
"https://thhrecruitment.co.uk/contact/",
"https://conceptrecruitment.com/contact-us/",
"https://www.essentialrecruitment.co.uk/contact-us/contact-the-management/",
"https://optimise-recruitment.co.uk/contact/",
"https://wise-recruitment.co.uk/contact-us/",
"https://journeyrecruitment.co.uk/",
"https://www.right-recruitment.com/contact.php",
"https://xpertrecruitmentltd.co.uk/contact-us/",
"https://i2irecruitment.co.uk/contact-us/",
"https://www.precision-people.uk/",
"https://www.pathrecruitment.com/?source=google.com",
"https://responserecruitment.co.uk/our-offices/",
"https://www.prosperity.ie/contact",
"https://ecsrecruitment.ie/contact-us/",
"https://hallrecruitment.ie/contact-us/",
"https://www.prcrecruitment.ie/",
"https://allenrec.com/contact-us/",
"www.sigmarrecruitment.com",
"https://focusedrecruitment.co.uk/"
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
