import os.path
import sys

def get_lines(file_name):
    try:
        count = 0
        with open(file_name, 'r') as file_one:
            for line in file_one:
                if not (line.lstrip().startswith("#") or line.strip()==""):
                    count+=1
            return count
    except:
        sys.exit("File does not exist")

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if ".py" in sys.argv[1]:
        file_name = sys.argv[1]
        no_of_lines = get_lines(file_name)
        print(no_of_lines)
    else:
        sys.exit("Not a Python file")
