import re

text = "Please contact support@example.com or sales@example.org for assistance."

pattern = r"\b\w+@\w+\.\w+\b"
emails = re.findall(pattern, text)

print("Email Addresses Found:", emails)
