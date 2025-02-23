company = {
    "employees": [
        {"name": "Alex", "position": "Manager", "salary": 5000},
        {"name": "Spongebob", "position": "Developer", "salary": 4000},
        {"name": "Patrick", "position": "Designer", "salary": 3500}
    ]
}

company["employees"].append({"name": "David", "position": "Analyst", "salary": 4500})

print("Employee Names:")
for employee in company["employees"]:
    print(employee["name"])
