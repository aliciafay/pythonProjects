#alicia
#remove, not replace, remove

def main():
    food=['pizza','burger','chips']
    print("Here are your food items")
    print(food)
    item=input("Which item should I remove?")

    try:
        #remove the item
        food.remove(item)
        print("Here is your new list")
        print(food)
    except ValueError:
        print("Item doesn't exist")
main()
