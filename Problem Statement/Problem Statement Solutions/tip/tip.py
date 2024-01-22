def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dollars = "".join(num for num in d if num.isdecimal())
    dollars = float(dollars)
    return dollars/100


def percent_to_float(p):
    # TODO
    percent = "".join(num for num in p if num.isdecimal())
    percent = float(percent)
    return percent/100

main()
