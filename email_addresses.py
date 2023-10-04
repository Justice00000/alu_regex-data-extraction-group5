import re

# Sample text containing email addresses
text = """
Email addresses:
- johndoe@example.com
- alice.smith@email.co.uk
- support@company.org
"""

# Define a regular expression pattern for email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Find all matches for email addresses
email_matches = re.findall(email_pattern, text)

# Print the extracted email addresses
print("\nExtracted Email Addresses:")
for email in email_matches:
    print("Email:", email)
