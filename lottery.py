#Alicia Leslie
#Lottery Program

import random
count=0

#generate two digit numner
computenumber=random.randint(10,99)
computenumber=str(computenumber)

#prompt user to enter two-digit number
lottery=input("Enter a two-digit number:")

#determine winning
if int(lottery)==int(computenumber):
    print("Exact match! You win $10,000")
elif int("%s%s" % (lottery[1], lottery[0])) == int(computenumber):
    print("Both numbers matched! You win $3000")
elif lottery[1]==computenumber[0] or lottery[0]==computenumber[1] or \
   lottery[1]==computenumber[1] or lottery[0]==computenumber[0]:
    print("One number matched! You win $1000")
else:
    print("You lose!")
