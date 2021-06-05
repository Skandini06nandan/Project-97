import random
print("Welcome to word guessing game!")
name = input("Enter your name")
print("Let's Play", name)
randomnumber = random.randint(0,9)
guess=1
while guess<=4:
    guessnumber=int(input("Enter a guess number between 0 to 9."))
    if guessnumber==randomnumber:
        print("Congrats you won!")
    elif guessnumber<randomnumber:
        print("Your guess is too low")
    elif guessnumber>randomnumber:
        print("Your guess is too high")
    guess=guess+1
if guessnumber!=randomnumber:
    print("Sorry! You lost the game")