# Dependencies
import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal_without_header.csv")

# Open and read csv
with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Iterate throught each row
    for row in csvreader:

        # Convert row to float and compare to grams of fiber
        if float(row[7]) >=5:
            print(row)
