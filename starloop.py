base_size=int(input("Enter triangle base size"))
for r in range(base_size, 0, -1):
    for c in range(r):
        print('*',end='')
    print()
