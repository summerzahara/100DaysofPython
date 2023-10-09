from sheety_alt import user_data
from icecream import ic

user_input = True
while user_input:
    print("Welcome to Summer's Flight Club.\nWe find the best flight deals and email you.")
    f_name = input("What is your first name?")
    l_name = input("What is your last name?")
    email1 = input("What is your email?")
    email2 = input("Type your email again")
    if email1 == email2:
        print("You're in the club!")
        new_user = {
            "firstName": f_name,
            "lastName": l_name,
            "email": email1,
        }
        user_data.append(new_user)
        user_input = False
ic(user_data)