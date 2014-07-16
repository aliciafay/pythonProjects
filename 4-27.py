#alicia
#4-27
#program reads list from file

def main():
    infile=open('cities.txt','r')
    cities=infile.readline()

    index=0
    while index<len(cities):
        cities[index]=cities[index].rstrip('\n')
        index+=1
    print(cities)
    infile.close()
main()
