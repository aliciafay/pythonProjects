#alicia
#4-13
#2D list - fill with random numbers
import random

rows=3
cols=4

def main():
    values=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for r in range(rows):
        for c in range(cols):
            values[r][c]=random.randint(1,100)
    print(values)
main()
