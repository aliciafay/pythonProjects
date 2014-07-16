import os

def delete():
    found=False
    search=input("Which coffee do you want to delete?")
    coffee_file=open('coffee.txt','r')
    temp_file=open('temp.txt','w')
    descr=coffee_file.readline()

    while descr!='':
        qty=float(coffee_file.readline())
        descr=descr.rstrip('\n')

        if descr!=search:
            temp_file.write(descr+'\n')
            temp_file.write(str(qty)+'\n')
        else:
            found=True
        descr=coffee_file.readline()
    coffee_file.close()
    temp_file.close()
    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
delete()
