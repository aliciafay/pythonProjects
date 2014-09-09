#Alicia Leslie
#This program calculates average of 3 test scores

test1=int(input("Enter Test Score 1:"))
test2=int(input("Enter Test Score 2:"))
test3=int(input("Enter Test Score 3:"))

avg=(test1+test2+test3)/3

print("The average score is:", avg)
if 90<=avg<=100:
    print("A")
if 80<=avg<=89:
    print("B")
if 70<=avg<=79:
    print("C")
if 0<=avg<=69:
    print("F")
if avg>100:
    print("Out of range")
if avg<0:
    print("Out of range")
