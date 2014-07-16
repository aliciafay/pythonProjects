#ex2 lab 14
#alicia leslie

#Paper, Rock, Scissors

import random
count=0

while count<=2 and count>=-2:
    computernumber=random.randint(0,2)
    
    usernumber=int(input("scissors(0),rock(1),paper(2):"))

    if computernumber==0:
        if usernumber==0:
            print("Draw")
        elif usernumber==1:
            print("You won")
            count+=1
        elif usernumber==2:
            print("You lose")
            count-=1

    if computernumber==1:
        if usernumber==1:
            print("Draw")
        elif usernumber==2:
            print("You won")
            count+=1
        elif usernumber==0:
            print("You lose")
            count-=1

    if computernumber==2:
        if usernumber==2:
            print("Draw")
        elif usernumber==0:
            print("You won")
            count+=1
        elif usernumber==1:
            print("You lose")
            count-=1

if count>2:
    print("You won more than 2 times")
else:
    print("The computer won more than 2 times")
