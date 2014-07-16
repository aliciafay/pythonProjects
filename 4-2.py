#alicia leslie
#4-2
#program to allow user to input values into a list

def main():
    #allow user to enter sales for 5 days, can change
    ndays=5
    #create list to hold sales
    sales=[0]*ndays
    index=0
    print("Enter sales for each day:")
    #get sales for each day
    while index<ndays:
        print("Day",index+1,';',sep='',end='')
        sales[index]=float(input())
        index+=1
    #display
    print("Here are the values entered")
    for value in sales:
        print(value)
main()
