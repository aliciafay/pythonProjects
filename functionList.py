#alicia
#program uses function to create a list and return to main and print

def main():
    numbers=get_values()
    print("The numbers in the list are:")
    print(numbers)

def get_values():
    values=[]
    again='Y'
    while again.upper()=='Y':
        num=int(input("Enter a number:"))
        values.append(num)
        print("Do you want to add another number?")
        again=input("y=yes,n=no")
        print()
    return values
main()
