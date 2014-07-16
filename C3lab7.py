#alicia leslie
#lab 7
#function to input data

def load():
    name=input("Enter a name:")
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    num3=int(input("Enter number 3:"))
    return name,num1,num2,num3
def calc(num1,num2,num3):
    sum=num1+num2+num3
    avg=sum/3
    return sum,avg
def output(name,n1,n2,n3,s,a):
    print("Your name is:",name)
    print("The 3 numbers are:",n1,n2,n3)
    print("The average is:",a)
    print("The sum is:",s)
def main():
    name,n1,n2,n3=load()
    sum,avg=calc(n1,n2,n3)
    output(name,n1,n2,n3,sum,avg)
main()
