#TRANSACTION MANAGEMENT SYSTEM

balance = 0

def main():
    #Max limit in balance
    max_limit = int(input("Enter Maximum limit for the account: "))
    with open("transaction_details.txt", 'w') as file:
        file.write(f"Category | Note | Amount\n")
    total = 0
    #Different choices of gain,loss transaction, display transaction, exit program
    while True:
        print("Enter a choice\n1.Add a credited Transaction\n2.Add a deducted transaction\n3.Display Transactions\n4.Exit")
        choice = int(input("Choice: "))
        if choice==1:
            amount_add = int(input("Enter the amount: "))
            amt1 = gain_transaction(amount_add,max_limit)
            if amt1 == type(int):
                total+=amt1
            else:
                print(amt1)
        elif choice==2:
            amount_sub = int(input("Enter the amount: "))
            amt2 = loss_transaction(amount_sub)
            if amt2 == type(int):
                total-=amt2
            else:
                print(amt2)
        elif choice==3:
            lines = display_transaction()
        elif choice==4:
            print("Balance: ",balance)
            break
        else:
            print("Enter a valid choice")



def gain_transaction(n,max_amount):
    global balance
    #if condition for checking if amount is not more than maximum limit
    if balance+n>max_amount:
        return ('Storage Full')
    else:
        category = input("Enter category: ")
        note = input("Enter note: ")
        #stores category and note information in a txt file
        with open("transaction_details.txt", 'a') as file:
            file.write(f"{category} | {note} | +{n}\n")
        balance+=n
        return balance


def loss_transaction(n):
    global balance
    #if condition for checking if amount is not more than the balance amount
    if balance-n<0:
        return ("Low Balance")
    else:
        category = input("Enter category: ")
        note = input("Enter note: ")
        #stores category and note information in a txt file
        with open("transaction_details.txt", 'a') as file:
            file.write(f"{category} | {note} | -{n}\n")
        balance-=n
        return balance


def display_transaction():
    #opens the txt file
    with open('transaction_details.txt', 'r') as file:
        lines = file.readlines()

    #lines variable contains a list of transactions and it is printed using a for loop
    for line in lines:
        print(line, end='')
    print('Balance: ',balance)
    return lines

if __name__ == "__main__":
    main()
