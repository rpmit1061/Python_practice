import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        secound = random.randint(1, 6)
        return first, secound


play = Dice()
print(play.roll())
from pathlib import Path

#Absolute path
# c:\Program Files\Microsoft

path = Path()
for file in path.glob('*.py'):
    print(file)

