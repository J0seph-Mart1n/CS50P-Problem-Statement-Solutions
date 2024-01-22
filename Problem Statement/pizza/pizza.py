import sys
import csv
from tabulate import tabulate

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if ".csv" in sys.argv[1]:
        file_name = sys.argv[1]
    else:
        sys.exit("Not a CSV file")

try:
    table = None
    with open(file_name, 'r') as csv_file:
        content = csv.reader(csv_file)
        table = tabulate(content, headers="firstrow", tablefmt='grid')
        print(table)
except FileNotFoundError:
    sys.exit("File does not exists")
