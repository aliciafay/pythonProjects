#alicia leslie
#recursion (fact)


def fact(n):
    if n ==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*(fact(n-1))

    
def main():
    n=int(input("Enter a nonnegative number:"))
    
    f=fact(n)
    print("The factorial of",n,"is",f)
main()
