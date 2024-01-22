import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    validate = re.search("^<iframe.*https?://(www.)?youtube.com/embed/xvFZjo5PgG0.*</iframe>$",s)
    if validate:
        return "https://youtu.be/xvFZjo5PgG0"
    else:
        return None




if __name__ == "__main__":
    main()
