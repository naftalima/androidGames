import csv

with open('gamename.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
"""
    for row in reader:
        for column in row:
            if column[0] == "timestamp":
                for cell in column :
"""