def search():
    found=False
    search=input("Enter a description to search for:")
    coffee_file=open('coffee.txt','r')
    descr=coffee_file.readline()
    while descr!='':
        qty=float(coffee_file.readline())
        descr=descr.rstrip('\n')

        if descr==search:
            print("Description:", descr)
            print("Quantity:", qty)
            print()
            found=True
        descr=coffee_file.readline()
    coffee_file.close()

    if not found:
        print("That item was not found in the file.")
search()
