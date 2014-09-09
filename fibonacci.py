#alicia leslie
#fibonacci

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def main():
    n=int(input("Enter Fib:"))
    print("The fib series are")
    for i in range(1,n+1):
        print(fib(i))
main()
