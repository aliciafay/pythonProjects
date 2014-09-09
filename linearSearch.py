#alicia leslie
#linear search

def findsort(something,alist):
    for item in alist:
        if item==something:
            return 'Found'
    return 'Not Found'
def main():
    print(findsort("bear",["apple","bear","cat","dog","elephant"]))
main()
