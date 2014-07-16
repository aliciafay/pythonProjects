#alicia
#4-22
#read with loop one line at a time until end of file

def main():
    sales_file=open('sales.txt','r')

    line=sales_file.readline()
    while line!='':
        amount=float(line)
        print(format(amount,'.2f'))
        line=sales_file.readline()
    sales_file.close()
main()
