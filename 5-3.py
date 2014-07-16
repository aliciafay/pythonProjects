#alicia leslie
#5-3
#binary search

import bubble

def binarySearch(lst,key):
    low=0
    high=len(lst)
    while high>=low:
        mid=(low+high)//2
        if key<lst[mid]:
            high=mid-1
        elif key==lst[mid]:
            return 'Found'
        else:
            low=mid+1
    return 'Not Found'
def main():
    lst1=[11,4,7,10,2,45,50,79,60,66,69,70,59]
    lst=bubble.bubblesort(lst1)
    print(lst)
    print(binarySearch(lst,2))
    print(binarySearch(lst,11))
    print(binarySearch(lst,12))
    print(binarySearch(lst,1))
    print(binarySearch(lst,3))
main()
    
