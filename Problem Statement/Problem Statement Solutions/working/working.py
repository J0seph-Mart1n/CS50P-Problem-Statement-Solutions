import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    validate = re.search("([0-9]|[1][0-2])(:[0-5][0-9])? (AM|PM) to ([0-9]|[1][0-2])(:[0-5][0-9])? (AM|PM)",s)

    if validate:
        time1 = validate.group(1)
        time2 = validate.group(4)
        if validate.group(3) == "PM":
            start = int(time1)+12
        else:
            start = int(time1)
        if validate.group(6) == "PM":
            end = int(time2)+12
        else:
            end = int(time2)
        if start==12 and validate.group(3) == "AM":
            start = 0
        if end==24 and validate.group(6) == "PM":
            end = 12
        if start<=9:
            start = str(start)
            start = "0"+start
        if end<=9:
            end = str(end)
            end = "0"+end
        if validate.group(2)==None and validate.group(5)==None:
            return f"{start}:00 to {end}:00"

        return f"{start}{validate.group(2)} to {end}{validate.group(5)}"
    else:
        raise ValueError



if __name__ == "__main__":
    main()
