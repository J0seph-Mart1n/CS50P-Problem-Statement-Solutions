import random
import sys


n = input("Level: ")
while n.isalpha() or int(n)<0:
    n = input("Level: ")

while True:
    guess = input("Guess: ")
    while guess.isalpha() or int(guess)<0:
        guess = input("Guess: ")
    if int(n)==1:
        print("Just right!")
        sys.exit()
    num = random.randrange(1,int(n))
    if num==int(guess):
        print("Just right!")
        sys.exit()
    elif num>int(guess):
        print("Too small!")
    else:
        print("Too large!")

