import csv

csv_file = "people.csv"
people_data = [["Name", "Age", "City"],
               ["Roma", "30", "New York"],
               ["Tokha", "25", "Los Angeles"],
               ["Susie", "35", "Chicago"]]

with open(csv_file, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(people_data)
print("Data has been written to", csv_file)

print("Reading data from the CSV file:")
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)