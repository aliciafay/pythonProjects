def sum(i1,i2):
    result=0
    for i in range(i1,i2+1):
        result+=i
    return result
def main():
    print("sum from 1 to 10",sum(1,10))
    print("sum from 20 to 37",sum(20,37))
    print("sum from 35 to 49",sum(35,49))
main()
