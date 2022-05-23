def loop_ints():
    current_number = 1
    while current_number <=5:
        print (current_number)
        current_number += 1

def loop_input():
    message = ""
    while message != 'quit':
        message = input("enter a message:")
        print ("you entered "+ message + "!")

def loop_flag_input():
    active = True
    while active:
        message = input("enter a message:")
        print ("you entered "+ message + "!")
        active = message != 'quit'

def while_with_break():
    prompt = "\nPlease enter the name of a city you have visited:"
    prompt += "\n(Enter 'quit' when you are finished.) "
    while True:
        city = input(prompt)
        if city == 'quit':
            break
        else:
            print ("I would like to go to "+city + "!")

def loop_continue():
    num = 1;
    while num <10:
        num+=1
        if num%2==0:
            continue
        print (num)
        

loop_ints()
#loop_input()
#loop_flag_input()
#while_with_break()
loop_continue()
