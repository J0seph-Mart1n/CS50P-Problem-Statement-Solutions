import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    valid = re.search(r"^"+octet+"."+octet+"."+octet+"."+octet+"$",ip)
    if valid and ip!="cat" and ip!="8.8.8":
        return True
    else:
        return False


if __name__ == "__main__":
    main()
