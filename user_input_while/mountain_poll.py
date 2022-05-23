responses = {}
polling_active = True

while polling_active:
    name = input("\n what is ur name? ")
    response = input("Which mountain do you want to climb someday?")
    responses[name] = response
    repeat = input("Would you like to other person respond (yes/no) ")
    polling_active = repeat=='yes'

print("poll results")
for name, response in responses.items():
    print(name.title() + " would like to climb "+response + ".")