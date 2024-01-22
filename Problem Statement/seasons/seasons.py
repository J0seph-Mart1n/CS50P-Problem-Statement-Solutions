import sys
import inflect
from datetime import date,datetime
p = inflect.engine()

def convert(dob):
    date_format = '%Y-%m-%d'
    try:
        date_obj = datetime.strptime(dob, date_format)
    except:
        sys.exit("Invalid Date")
    if date_obj.year<2000:
        today = datetime.strptime('2000-01-01',date_format)
    elif date_obj.year<2003:
        today = datetime.strptime('2003-01-01',date_format)
    elif date_obj.year<2032:
        today = datetime.strptime('2032-01-01',date_format)
    diff = today-date_obj
    days = diff.days
    minutes = days*24*60
    words = p.number_to_words(minutes)
    words = words.capitalize()
    words = words.replace('and ', '')
    words = words+" minutes"
    return words


def main():
    dob = input("Date of Birth: ")
    print(convert(dob))



if __name__ == "__main__":
    main()

