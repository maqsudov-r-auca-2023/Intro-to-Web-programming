import re

text1 = "Hello, how are you?"
text2 = "Say Hello to everyone."

pattern = r"^Hello"

match1 = re.match(pattern, text1)
match2 = re.match(pattern, text2)

search2 = re.search(pattern, text2)

print("Using re.match() on text1:")
print("Match found:", match1.group() if match1 else "No match found.")

print("\nUsing re.match() on text2:")
print("Match found:", match2.group() if match2 else "No match found.")

print("\nUsing re.search() on text2:")
print("Found:", search2.group() if search2 else "No match found.")
