import pyfiglet
from pyfiglet import Figlet
import sys
Figlet = Figlet()
fonts = Figlet.getFonts()
try:
    if len(sys.argv)==3:
        if (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
            if sys.argv[2] in fonts:
                input = input("Input: ")
                output = pyfiglet.figlet_format(input,font=sys.argv[2])
                print(output)
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv)==1:
        input = input("Input: ")
        output = pyfiglet.figlet_format(input)
        print(output)
    else:
        sys.exit("Invalid usage")
except:
    sys.exit("Invalid usage")


