#alicia leslie
#5-2
#bubblesort

def bubblesort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if (lst[j]>lst[j+1]):
                t=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=t
    return lst

lst=[2,30,55,23,45,89,12,35,11,28,1,9]
lst2=bubblesort(lst)

print(lst2)



            

