def make_pizza(requested_toppings):
    for topping in requested_toppings:
        print("Adding "+topping)
    print("\nFinished making pizza\n")

def conditional_make_pizza(requested_toppings):
    if 'mushrooms' in requested_toppings:
        print("Adding mushroom")
    if 'green peppers' in requested_toppings:
        print("Sorry, we're out of green peppers")
    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese")
    print("\nFinished making pizza!")

def empty_list_check(requested_toppings):
    if(requested_toppings):
        make_pizza(requested_toppings)
    else:
        print("\nit's empty toppings list, do you want a plain pizza")

requested_toppings = ['mushrooms', 'extra cheese']
make_pizza(requested_toppings)
conditional_make_pizza(requested_toppings=['mushrooms','green peppers'])
empty_list_check([])