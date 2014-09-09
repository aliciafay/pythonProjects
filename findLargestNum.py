#alicia leslie
#find largest number

num=int(input("Enter a value"))
large=int(input("Enter a value"))
while num!=-999:
    if num>large:
        large=num
    num=int(input("Enter a value or -999 to quit"))
print("The largest number is",large)
