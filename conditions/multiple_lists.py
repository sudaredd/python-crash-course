def multiple_list_conditions(available_toppings, required_toppings):
    for required_topping in required_toppings:
        if required_topping in available_toppings:
            print('Adding '+required_topping + ".")
        else:
            print("Sorry, we don't have "+ required_topping + ".")
    print("\nFinished making your pizza!")
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
required_toppings = ['mushrooms', 'french fries', 'extra cheese']
multiple_list_conditions(available_toppings, required_toppings)
