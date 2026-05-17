import os
import shutil
import re
import requests

print("=" * 40)
print("   TASK 3: Automation Script")
print("=" * 40)

# ----------------------------------------
# TASK 1: Move .jpg files to a new folder
# ----------------------------------------
print("\n[1] Moving .jpg files...")

source_folder = "/storage/emulated/0"
destination_folder = "/storage/emulated/0/jpg_images"

try:
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"    Created folder: 'jpg_images'")

    jpg_files = [f for f in os.listdir(source_folder)
                 if f.lower().endswith(".jpg") and
                 os.path.isfile(os.path.join(source_folder, f))]

    if not jpg_files:
        print("    No .jpg files found.")
    else:
        moved = 0
        for filename in jpg_files:
            src = os.path.join(source_folder, filename)
            dst = os.path.join(destination_folder, filename)
            if os.path.exists(dst):
                print(f"    Skipped (already exists): {filename}")
            else:
                shutil.move(src, dst)
                print(f"    Moved: {filename}")
                moved += 1
        print(f"    Done! Moved {moved} file(s) to 'jpg_images'.")

except Exception as e:
    print(f"    Error: {e}")

# ----------------------------------------
# TASK 2: Extract emails from input.txt
# ----------------------------------------
print("\n[2] Extracting emails...")

input_file  = "/storage/emulated/0/input.txt"
output_file = "/storage/emulated/0/emails.txt"

try:
    with open(input_file, "r") as f:
        text = f.read()

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = sorted(set(email.lower() for email in re.findall(pattern, text)))

    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    if emails:
        print(f"    Found {len(emails)} unique email(s). Saved to emails.txt")
        for email in emails:
            print(f"    -> {email}")
    else:
        print("    No emails found in input.txt")

except FileNotFoundError:
    print("    'input.txt' not found.")
    print("    Creating a sample input.txt for you...")
    with open(input_file, "w") as f:
        f.write("Hello contact test@gmail.com and hello@yahoo.com and admin@example.com\n")
    print("    Sample input.txt created! Run the script again.")

except Exception as e:
    print(f"    Error: {e}")

# ----------------------------------------
# TASK 3: Scrape webpage title
# ----------------------------------------
print("\n[3] Scraping webpage title...")

url = "https://www.wikipedia.org"

try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Android; Mobile; rv:109.0) Gecko/109.0 Firefox/109.0"
    }
    response = requests.get(url, timeout=10, headers=headers)
    response.raise_for_status()

    pattern = r"<title>(.*?)</title>"
    match = re.search(pattern, response.text, re.IGNORECASE)

    if match:
        title = match.group(1).strip()
        print(f"    Title: {title}")

        with open("/storage/emulated/0/webpage_title.txt", "w") as f:
            f.write(f"URL   : {url}\n")
            f.write(f"Title : {title}\n")

        print("    Saved to webpage_title.txt")
    else:
        print("    No title found on the page.")

except requests.exceptions.ConnectionError:
    print("    No internet connection.")
except requests.exceptions.Timeout:
    print("    Request timed out.")
except Exception as e:
    print(f"    Error: {e}")

# ----------------------------------------
print("\n" + "=" * 40)
print("   All tasks completed!")
print("=" * 40)

