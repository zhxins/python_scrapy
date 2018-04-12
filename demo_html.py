from random import randint
from demo_mm1 import tt

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

if __name__ == "__main__":

    die = Die()
    res = die.roll()
    print(res)