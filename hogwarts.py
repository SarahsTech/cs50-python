# imports a csv file with student names and houses
import csv


# open the csv file named students.csv
# newline="" prevents blank lines from appearing between rows on Windows
with open("students.csv", newline='') as file:
    # create a DictReader object which reads each raw as a dictionary
    reader = csv.DictReader(file)

    print("name       house        patronus")
    # loop through each row (dictionary) in the csv file
    for row in reader:
        # row['name'] gets the value under the name column
        # row['house'] gets the value under the house column
        print(f"{row['name']:<10} {row['house']:<12} {row['patronus']}")