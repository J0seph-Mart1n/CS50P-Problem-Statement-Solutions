a = []
try:
    while True:
        name = input("Name: ")
        a.append(name)
except EOFError:
    if len(a)==1:
        print(f"Adieu, adieu, to {a[0]}")
    elif len(a)==2:
        print(f"Adieu, adieu, to {a[0]} and {a[1]}")
    elif len(a)>2:
        len = len(a)
        str = ", ".join(a[0:len-1])
        print()
        print(f"Adieu, adieu, to {str}, and {a[len-1]}")
