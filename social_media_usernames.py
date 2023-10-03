#!/usr/bin/python3
import re

def extract_usernames(text):
    pattern = re.compile(r'@([a-zA-Z0-9_]+)')
    match = pattern.search(text)
    if match:
        return match.group(1)
    else:
        return None

# Test the function
raw_data = "Check out this tweet from @user123!"
result = extract_usernames(raw_data)

if result:
    print(f"Username: {result}")
else:
    print("No username found.")
