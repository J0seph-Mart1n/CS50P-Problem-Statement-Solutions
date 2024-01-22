import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    list1 = re.findall("([, ]+um[,. ]+|^um[.,?]|^um$)",s, re.IGNORECASE)

    return len(list1)

if __name__ == "__main__":
    main()
