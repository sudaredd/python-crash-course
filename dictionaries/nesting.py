from hashlib import new


def print_aliens(aliens):
    for alien in aliens:
        print(alien)

def make_30_aliens():
    aliens = get_aliens(30)
    for alien in aliens[0:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['points'] = 10
    
    #show first 5 aliens
    for al in aliens[:5]:
        print(al)
    #show number of aliens created
    print("Total number of aliens created "+str(len(aliens)))

def get_aliens(count):
    aliens = []
    for alien_number in range(count):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow', 'number':alien_number}
        aliens.append(new_alien)
    return aliens
    
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

print_aliens(aliens)
make_30_aliens()