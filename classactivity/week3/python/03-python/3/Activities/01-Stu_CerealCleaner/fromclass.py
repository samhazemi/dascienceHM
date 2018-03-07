import csv
import os
cereal_csv=os.path.join("Resources","cereal.csv")
with open(cereal_csv,newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
#    print(csvreader)
    for row in csvreader:
        if float(row[7]) >=5:
            print(row)
