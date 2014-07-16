#Program 1
#Alicia Leslie
#214236
#Lottery Program

import random

lott=random.randint(10,99)

guess=int(input("Enter your two digit lottery number"))

lottdig1=lott//10
lottdig2=lott%10

guessdig1=guess//10
guessdig2=guess%10

if guess==lott:
    print("Exact match! You win $10,000")
elif (guessdig2==lottdig1 and guessdig1==lottdig2):
    print("Both numbers matched! You win $3000")
elif (guessdig1==lottdig1 or guessdig1==lottdig2 or \
      guessdig2==lottdig1 or guessdig2==lottdig2):
    print("One number matched! You win $1000")
else:
    print("You lose!")

