import re

text = "There are 10 apples, 20 oranges, and 30 bananas in the basket."

pattern = r"\d+"
modified_text = re.sub(pattern, "NUMBER", text)

print("Modified Text:", modified_text)
