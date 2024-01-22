from datetime import datetime
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
try:
    date = input("Date: ").strip()
    if "/" in date:
        format2 = "%m/%d/%Y"
        obj2 = datetime.strptime(date, format2)
        d2 = obj2.strftime("%Y-%m-%d")
        print(d2)

    for i in range(len(months)):
        if months[i] in date:
            format1 = "%B %d, %Y"
            obj1 = datetime.strptime(date, format1)
            d1 = obj1.strftime("%Y-%m-%d")
            print(d1)
except:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            format2 = "%m/%d/%Y"
            obj2 = datetime.strptime(date, format2)
            d2 = obj2.strftime("%Y-%m-%d")
            print(d2)

        for i in range(len(months)):
            if months[i] in date:
                format1 = "%B %d, %Y"
                obj1 = datetime.strptime(date, format1)
                d1 = obj1.strftime("%Y-%m-%d")
                print(d1)
    except:
        pass
