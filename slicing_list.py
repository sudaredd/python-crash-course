def main(args):
    slice_list()
    loop_slice_list()
    copy_list()

def copy_list():
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    print(my_foods)
    print(friend_foods)
    my_foods.append("chicken biryani")
    friend_foods.append("chicken curry")
    print(my_foods)
    print(friend_foods)

def loop_slice_list():
    print("loop_slice_list start")
    players = get_players()
    for player in players[:2]:
        print(player.title())
    print("loop_slice_list end")


def slice_list():
    players = get_players()
    print(players[0:3])
    print(players[:4])
    print(players[2:])

def get_players():
    players = ["charles", "martina", "inna", "ana", "elina"]
    return players

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))