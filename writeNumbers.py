#alicia
#program to write numbers to file

def main():
    outfile=open('numbers.txt','w')

    num1=int(input('Enter a number'))
    num2=int(input('Enter a number'))
    num3=int(input('Enter a number'))


#convert number to string
    outfile.write(str(num1)+'\n')
    outfile.write(str(num2)+'\n')
    outfile.write(str(num3)+'\n')

    outfile.close()
main()
