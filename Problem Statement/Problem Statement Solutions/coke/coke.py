amount = 50

while amount!=0:
    coin = int(input("Insert Coin: "))
    if coin in [5,10,25]:
        if coin>=amount:
            print("Change Owed:", (coin-amount))
            break
        elif coin==5:
            amount-=5
            print("Amount Due:", amount)
        elif coin==10:
            amount-=10
            print("Amount Due:", amount)
        elif coin==25:
            amount-=25
            print("Amount Due:", amount)
    else:
        print("Amount Due:", amount)
