#alicia
#program reads list from file

def main():
    infile=open('cities.txt','r')
    cities=infile.readline()

    index=0
    while cities:
        index+=1
        print(cities.rstrip('\n'))
        cities = infile.readline()

    infile.close()

main()
