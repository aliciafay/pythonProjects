#alicia
#program asks user for 3 names to write to file

def main():
    print('Enter three names')
    name1=input('name 1:')
    name2=input('name 2:')
    name3=input('name 3:')

    my_file=open('friends.txt','w')

    my_file.write(name1+'\n')
    my_file.write(name2+'\n')
    my_file.write(name3+'\n')

    my_file.close()
main()
