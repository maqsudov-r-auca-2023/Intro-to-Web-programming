file_name = "sample_text.txt"
with open(file_name, "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text for testing file operations.\n")
print("Content has been written to", file_name)

with open(file_name, "r") as file:
    content = file.read()
print("Content read from the file:")
print(content)
