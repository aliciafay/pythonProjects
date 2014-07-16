def menu():
    record=1
    while record!=-999:
        print("-------------------------")
        print("1 - Add coffee:")
        print("2 - Delete coffee:")
        print("3 - Modify coffee:")
        print("4 - Search for coffee:")
        print("5 - Show coffee records:")
        print()
        record=int(input("Enter a number to manage coffee or -999 to quit:"))

        if record==1:
            from add_coffee_record import add
        elif record==2:
            from delete_coffee_record import delete
        elif record==3:
            from modify_coffee_record import modify
        elif record==4:
            from search_coffee_record import search
        else:
            from show_coffee_record import show
menu()
