#alicia
#Append

def main():
    #create an empty list
    name_list=[]
    #create a variable to control loop/flag
    again='Y'

    while again.upper()=='Y':
        name=input("Enter name:")
        name_list.append(name)
        print("Do you want to add another name?")
        again=input("y=yes,n=no")
        print()
    print("Here are your names")
    for name in name_list:
        print(name)
main()
