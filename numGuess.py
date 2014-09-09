#alicia leslie
#guess a number from 1 to 100

import random
print("Guess my number between 1 to 100")

my_number=random.randint(1,100)
guess=int(input("Take a guess"))
tries=1

while guess!=my_number:
    if guess>my_number:
        print("lower")
    else:
        print("higher")

    guess=int(input("take a guess"))

    tries=tries+1

print("You guessed it! The number is",my_number)
print("You took",tries,"tries!\n")
