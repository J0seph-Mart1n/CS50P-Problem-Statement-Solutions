i=1
j=1
while i!=0:
    try:
        x,y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        i=0
    except ValueError:
        i=1
        x,y = input("Fraction: ").split("/")

k = 1
while k!=0:
    if x>y:
        x,y = input("Fraction: ").split("/")
        k = 1
    else:
        k=0

while j!=0:
    try:
        per = int(x)/int(y)
        j=0
    except ZeroDivisionError:
        x,y = input("Fraction: ").split("/")
        j=1

per = round((int(x)/int(y))*100)
if per<=1:
    print("E")
elif per>=99:
    print("F")
else:
    print(f"{per}%")
