import csv

with open ("spikes.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['time']}: {row['voltage']}")