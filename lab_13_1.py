import re

text = "Call me at 555-1234 or 555-5678. My office number is 555-9999."

pattern = r"\b\d{3}-\d{4}\b"
phone_numbers = re.findall(pattern, text)

print("Phone Numbers Found:", phone_numbers)
