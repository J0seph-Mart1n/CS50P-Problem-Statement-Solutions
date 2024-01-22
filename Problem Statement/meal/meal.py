from datetime import datetime

def main():
    time = input("What time is it? ")
    decimal_time = convert(time)
    #decimal_time = am_pm_convert()
    if 7<=decimal_time<=8:
        print("breakfast time")
    elif 12<=decimal_time<=13:
        print("lunch time")
    elif 18<=decimal_time<=19:
        print("dinner time")

def convert(time):
    time_obj = datetime.strptime(time, "%H:%M")
    hour = time_obj.strftime("%H")
    minutes = time_obj.strftime("%M")
    decimal = int(hour)+(int(minutes)/60)
    return decimal

#challenge
'''def am_pm_convert():
    format = int(input("Enter which format to choose (type 12 or 24): "))
    time = (input("What time is it? "))
    if format==12:
        time_obj = datetime.strptime(time, "%H:%M %p")
        hour = time_obj.strftime("%H")
        minutes = time_obj.strftime("%M")
        am_pm = time_obj.strftime("%p")
        if am_pm == "AM":
            decimal = int(hour)+(int(minutes)/60)
            return decimal
        elif am_pm == "PM":
            decimal = int(hour)+(int(minutes)/60)
            return decimal+12
    elif format==24:
        time_obj = datetime.strptime(time, "%H:%M")
        hour = time_obj.strftime("%H")
        minutes = time_obj.strftime("%M")
        decimal = int(hour)+(int(minutes)/60)
        return decimal
'''
if __name__ == "__main__":
    main()
