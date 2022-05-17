players = ["charles", "martina", "inna", "ana", "elina", "karina", "haseena"]

def main(args):
    do_4_10()
    do_4_11()

def do_4_11():
    my_pizzas = ['veg pizza', 'chicken pizza']
    friend_pizzas = my_pizzas[:]
    print(my_pizzas)
    print(friend_pizzas)
    my_pizzas.append('cheese pizza')
    friend_pizzas.append('Pepparoni')
    print(my_pizzas)
    print(friend_pizzas)

def do_4_10():
    first_3 = players[:3]
    print(first_3)
    middle = int(len(players)/2)
    print(players[middle:middle+3])
    last = len(players);
    print(players[last-3:])

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))