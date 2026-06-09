import time
import json
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from plyer import notification

URL = "https://mms.st-andrews.ac.uk/mms/module/2025_6/Y1/CS3099/CS3099+Coursework/Student" # link to coursework page

CHECK_INTERVAL = 60  # seconds

def extract_grades(html):
    soup = BeautifulSoup(html, "html.parser")
    # Skip to table of results
    rows = soup.select("#studentAssignmentsTable tbody tr")
    grades = {}

    for row in rows:
        cols = row.find_all("td")

        if len(cols) < 7:
            continue
        
        # Get assignment and grade values from table
        assignment = cols[0].get_text(strip=True)
        grade = cols[6].get_text().replace('\xa0', '').strip()

        grades[assignment] = grade

    return grades

# Create notification
def notify(title, message):
    print(f"{title}: {message}")

    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

# Playwright for launching browser notification
if __name__ == "__main__":
    # Playwright block guarded for modular testing
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context = browser.new_context(storage_state="auth.json")

        page = context.new_page()

        page.goto(URL)

        old_grades = extract_grades(page.content())

        print("Monitoring grades...")
        print(old_grades)

        while True:
            time.sleep(CHECK_INTERVAL)

            try:
                page.reload(wait_until="networkidle")

                new_grades = extract_grades(page.content())

                for assignment in new_grades:

                    old = old_grades.get(assignment, "")
                    new = new_grades.get(assignment, "")

                    # Detect newly released grades (if there has been an update)
                    if old != new:

                        if old == "" and new != "":
                            notify(
                                "New Grade Posted",
                                f"{assignment}: {new}"
                            )

                        else:
                            notify(
                                "Grade Changed",
                                f"{assignment}: {old} → {new}"
                            )

                old_grades = new_grades

            except Exception as e:
                print("Error:", e)