#alicia leslie

import loginNamePassword.py
def main():
    first=input("Enter first name:")
    last=input("Enter last name:")
    idnumber=input("Enter student id")
    print("Your system login name is:")
    print(C3lab10.get_login_name(first,last,idnumber))

    password=input("Enter new password:")

    while not C3lab10.valid_password(password):
        print("Password not valid")
        password=input("Enter new password")
    print("Valid password")
main()
