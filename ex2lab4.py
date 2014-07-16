#Lab 4
#Alicia Leslie
#214236
#This program calculates average of 3 test scores

test1=int(input("Enter Test Score 1:"))
test2=int(input("Enter Test Score 2:"))
test3=int(input("Enter Test Score 3:"))

avg=(test1+test2+test3)/3

print("The average score is:", avg)
if avg<0 or avg>100:
    print('invalid')
else:
    if avg>=90:
        print('A')
    else:
        if avg>=80:
            print('B')
        else:
            if avg>=70:
                print('C')
            else:
                if avg>=0:
                    print('F')

