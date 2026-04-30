import re

try:
    # Open the input file in read mode
    with open("input.txt", "r") as f:
        text = f.read()
        
    # The regular expression pattern to find emails
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    
    # Open the output file in write mode
    with open("emails.txt", "w") as f:
        for email in emails:
            f.write(email + "\n")
            
    print(f"Done! Found {len(emails)} email(s). Saved to emails.txt")
    
    if not emails:
        print("No emails found. Check your input.txt file.")
        
except FileNotFoundError:
    print("Oops! 'input.txt' doesn't exist. Please create it and add some text with emails in it before running.")
