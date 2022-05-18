def alien_color_1():
    if 'green' in alien_color:
        points = 5
    elif 'red' in alien_color:
        points = 10
    print("player just earned "+ str(points) + " points")

def alien_color_2():
    if 'green' in alien_color:
        print("the player just earned 5 points for shooting the alien\n")
    if 'green' not in alien_color:
        print("the player just earned 10 points for shooting the alien")

    alien_color1=['green1','yellow','red']

    if 'green' in alien_color1:
        print("the player just earned 5 points for shooting the alien")
    elif 'green' not in alien_color1:
        print("the player just earned 10 points for shooting the alien")

alien_color=['green','yellow','red']

alien_color_1()
alien_color_2()