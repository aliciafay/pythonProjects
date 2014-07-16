#lab 8
#alicia leslie
#temperature check program

MAX_TEMP=102.5

temp=float(input("Enter temp:"))

while temp>MAX_TEMP:
    print("temperature too high")
    print("Turn on AC")

    temp=float(input("Enter now temp"))

print("Temperature is cooler now")
print("Check again in 30 minutes")
