import requests
import sys

try:
    if len(sys.argv)!=2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        total = str(float(sys.argv[1])*float(data["bpi"]["USD"]["rate_float"]))
        print(f"${total[0:2]},{total[2:]}")

except requests.RequestException:
    pass
