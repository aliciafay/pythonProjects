#alicia
#4-4
#in operator

def main():
    #create list
    prod_name=['V4','F8','Q1','R6']
    #get prod name
    search=input("Enter a Product name:")

    if search in prod_name:
        print(search,'was found in list')
    else:
        print(search,'was not in list')
main()
