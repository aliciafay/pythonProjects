#Lab 3
#Alicia Leslie
#214236
#This program calculates average of 3 test scores

test1=int(input("Enter Test Score 1:"))
test2=int(input("Enter Test Score 2:"))
test3=int(input("Enter Test Score 3:"))

avg=(test1+test2+test3)/3

print("The average score is:", avg)
if avg>=90 and avg<=100:
    print("A")
if avg>=80 and avg<=89:
    print("B")
if avg>=70 and avg<=79:
    print("C")
if avg>=0 and avg<=69:
    print('F')
else:
    print('invalid')
