def make_pizza(size, *toppings):
    print("\nMaking "+str(size) + " inch pizza with the following toppings")
    for topping in toppings:
        print("- "+topping)

def build_profile(first, last, **user_info):
    """Build a dicitonary containing everything about user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, val in user_info.items():
        profile[key] = val
    return profile

make_pizza(16, 'peporroni')
make_pizza(12, 'mishroom','green pepper', 'spinach', 'onion')
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)