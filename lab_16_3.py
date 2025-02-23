import json

student_info = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

file_name = "student.json"

with open(file_name, "w") as file:
    json.dump(student_info, file, indent=4)

print(f"Data has been written to {file_name}")

with open(file_name, "r") as file:
    loaded_data = json.load(file)

print("Data loaded from the JSON file:")
print(loaded_data)
