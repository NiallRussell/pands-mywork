import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter = ",", quoting = csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: #if linecount = 0, this is False
        else
        total += int(line[0])
        print(line)
        linecount += 1