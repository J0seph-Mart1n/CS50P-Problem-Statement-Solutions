import random


def main():
    loop = 10
    score = 0
    count = 3
    level = get_level()
    while loop != 0:
        if count == 3:
            x, y = generate_integer(level)
        try:
            result = int(input(f"{x} + {y} = "))
            answer = x + y
            if result == answer:
                loop-=1
                score = score + 1
                count = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            count-=1
            pass
        if count == 0:
            print((f"{x} + {y} = {answer}"))
            count = 3
            loop-=1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
