from random import randint

class Dice():
    def __init__(self, sides):
        self.sides = sides
    
    def roll_dice(self):
        print("rolling for "+str(self.sides) + " sides")
        for i in range(1, 11):
            rn = randint(1, self.sides)
            print("random value of "+str(self.sides) + " sides at "+ str(i) + " th trail is "+str(rn))
        print("\n")
dice_6 = Dice(6)
dice_6.roll_dice()

dice_10 = Dice(10)
dice_10.roll_dice()

dice_20 = Dice(20)
dice_20.roll_dice()
