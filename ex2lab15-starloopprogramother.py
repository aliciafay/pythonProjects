base_size=int(input("Enter triangle base size"))
for r in range(base_size):
    for c in range(r + 1):
        print(c+1,end='')
    print()
