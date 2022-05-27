import json

def get_stored_user_name():
    filename = 'username.json'
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_user_name()
    if(username):
        print("Welcome back "+username)
    else:
        username = input("What is ur name? ")
        filename = 'username.json'
        with open(filename, 'w') as file_obj:
            json.dump(username, file_obj)
            print("We'll remember you when you come back, " + username + "!")
greet_user()