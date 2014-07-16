#alicia
#4-11
#program calculates the values of a list

def main():
    scores=[5,5,5]
    total=0.0
    for value in scores:
        total+=value
    average=total/len(scores)
    print(total,average)
main()
