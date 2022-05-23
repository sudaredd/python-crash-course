def list_while_for():
    unconfirmed_users=['pras','sudar','dvya','bvya']
    confirmed_users=[]
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)
# Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

def remove_specific():
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)

list_while_for()
remove_specific()
