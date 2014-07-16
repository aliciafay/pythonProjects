#ex2 lab 11
#alicia leslie

#allow user to enter the start and end range

start=int(input("Enter start number"))
end=int(input("Enter end number"))

print()
print('Number\t Square')
print('...................')

for number in range(start,end+1):
    square=number**2
    print(number,'\t',square)
