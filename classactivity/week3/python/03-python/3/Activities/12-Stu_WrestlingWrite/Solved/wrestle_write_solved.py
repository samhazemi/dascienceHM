# Part 1
import os
import csv

# List of year
wrestlingYears = ['2017', '2016', '2015', '2014']

# Loop through years
for yearToCheck in wrestlingYears:

    # Grab wrestling CSV
    wrestlingCSV = os.path.join('..', 'raw_data', 'WWE-Data-' + yearToCheck + '.csv')

    # Create new CSV
    newWrestlingCSV = os.path.join('..', 'output', 'WWE-Data-' + yearToCheck + '.csv')

    # Set empty list variables
    wrestlers = []
    wins = []
    winPercent = []
    losses = []
    lossPercent = []
    draws = []
    drawPercent = []

    # Open current wrestling CSV
    with open(wrestlingCSV, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)
        
        for row in csvReader:

            # Append data from the row
            wrestlers.append(row[0])
            wins.append(row[1])
            losses.append(row[2])
            draws.append(row[3])

            # Calculate percentages and append to the list
            winPercent.append(int(row[1])/(int(row[1]) + int(row[2]) + int(row[3]))*100)

            lossPercent.append(int(row[2])/(int(row[1]) + int(row[2]) + int(row[3]))*100)

            drawPercent.append(int(row[3])/(int(row[1]) + int(row[2]) + int(row[3]))*100)

    # Zip lists together
    cleanCSV = zip(wrestlers, wins, losses, draws, winPercent, lossPercent, drawPercent)

    with open(newWrestlingCSV, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(["Wrestler","Wins","Losses","Draws","Win Percent","Loss Percent","Draw Percent"])

        # Write the zipped lists to a csv
        csvWriter.writerows(cleanCSV)
