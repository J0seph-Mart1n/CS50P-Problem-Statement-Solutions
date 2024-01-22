def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    x,y = fraction.split("/")
    if int(x)/int(y)>1:
        raise ValueError
    elif int(y)==0:
        raise ZeroDivisionError

    percentage = round((int(x)/int(y))*100)
    return percentage

def gauge(percentage):
    try:
        if percentage<=1:
            return ("E")
        elif percentage>=99:
            return ("F")
        elif 1<percentage<99:
            return (f"{percentage}%")
        else:
            raise TypeError
    except TypeError:
        pass

if __name__ == "__main__":
    main()
