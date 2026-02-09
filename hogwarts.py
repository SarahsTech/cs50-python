import csv

with open("students.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['house']}")