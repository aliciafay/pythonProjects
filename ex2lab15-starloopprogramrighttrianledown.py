base_size=int(input("Enter triangle base size"))
for r in range(base_size, 0, -1):
    for d in range(r - 1):
        print(" ", end='')
    for c in range(base_size - r + 1):
        print('*',end='')
    print(" ")
