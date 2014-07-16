#alicia
#4-7
#index method

def main():
    food=['pizza','burger','chips']
    print("Here are your food items")
    print(food)
    item=input("Which item should I change?")

    try:
        #get items index on list
        item_index=food.index(item)
        #get value to replace it
        new_item=input("Enter new food item:")
        #replace old item with new
        food[item_index]=new_item

        print("Here is your new food items")
        print(food)
    except ValueError:
        print("That item was not on the list")
main()
