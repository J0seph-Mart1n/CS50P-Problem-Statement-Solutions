import sys
import csv
from tabulate import tabulate

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    if ".csv" in (sys.argv[1] and sys.argv[2]):
        file_before = sys.argv[1]
        file_after = sys.argv[2]
    else:
        sys.exit("Not a CSV file")


    try:
        with open(file_before, 'r') as file1:
            content = csv.DictReader(file1)
            with open(file_after, 'w') as file2:
                fields = ["first", "last", "house"]
                writer = csv.DictWriter(file2, fieldnames = fields)
                writer.writeheader()
                for student in content:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first":first, "last":last, "house":house})
    except FileNotFoundError:
        sys.exit("File does not exists")

