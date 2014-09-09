#alicia leslie
#recursion (two)

def two(n):
    if n==0:
        return 1
    else:
        return 2*two(n-1)
def main():
    n=int(input("Enter a nonnegative number:"))
    t=two(n)
    print("The two to the power of",n,"is",t)
main()
