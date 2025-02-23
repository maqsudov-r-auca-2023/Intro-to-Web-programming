import json

json_string = '''
{
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
'''

python_dict = json.loads(json_string)

print("Deserialized Python object:")
print(python_dict)
