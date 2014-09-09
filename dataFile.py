#alicia
#4-14
#write data to file

def main():
    outfile=open('philosophers.txt','w')
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Broke\n')
    outfile.close()
main()
