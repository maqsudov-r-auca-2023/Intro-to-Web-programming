file_name = "sample_text.txt"

with open(file_name, "a") as file:
    file.write("This line is appended to the file.\n")
print("Additional text has been appended to", file_name)

with open(file_name, "r") as file:
    updated_content = file.read()
print("Updated content of the file:")
print(updated_content)
