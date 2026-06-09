from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://mms.st-andrews.ac.uk")

    print("Please log in manually.")
    input("Press ENTER after login completes...")

    context.storage_state(path="auth.json")

    print("Saved login session.")

    browser.close()