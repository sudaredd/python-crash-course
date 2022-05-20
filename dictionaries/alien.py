from cgi import print_directory
from os import remove


alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}
def print_dict():
    print(alien_0)

def add_dict():
    alien_0['x-position'] = 5
    alien_0['y-position'] = 10
    print_dict()

def modify_dict():
    alien_0['y-axis'] = 11
    print_dict()

def modify_dict_conditional():
    print_dict()
    if(alien_0['speed']=='slow'):
        x_increment = 1
    elif(alien_0['speed']=='medium'):
        x_increment = 2
    elif(alien_0['speed']=='fast'):
        x_increment = 3
    alien_0['x-position'] = alien_0['x-position'] + x_increment
    print_dict()

def remove_dict():
    del alien_0['y-axis']
    print_dict()

print_dict()
add_dict()
modify_dict()
modify_dict_conditional()
remove_dict()