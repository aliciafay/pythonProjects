base_size=int(input("Enter triangle base size"))
for r in range(base_size, 0, -1):
    for d in range(base_size - r):
        print(" ", end='')
    for c in range(r):
        print('*',end='')
    print(" ")
