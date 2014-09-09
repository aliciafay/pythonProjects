#alicia
#4-20
#read numbers back from file

def main():
    infile=open('numbers.txt','r')

    num1=int(infile.readline())
    num2=int(infile.readline())
    num3=int(infile.readline())
    infile.close()

    print(num1)
    print(num2)
    print(num3)
main()
