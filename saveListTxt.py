#alicia
#program to save a list to text_file

def main():
    cities=['New York','Boston','Alanta','Dallas']

    outfile=open('cities.txt','w')

    for item in cities:
        outfile.write(item+'\n')
    outfile.close()
main()
