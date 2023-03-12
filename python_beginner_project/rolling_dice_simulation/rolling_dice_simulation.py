import random

def dice_roll(dice, sides):
  roll = []

  for i in range(0,dice):
    face = random.randint(1,sides)
    roll.append(face)

  return roll

dice = int(input("Dice: "))

if (dice <= 0):
  print("Must have at least one dice!")
  quit()

sides = int(input("Sides: "))

if (sides <= 0):
  print("Must have at least one side!")
  quit()

roll = dice_roll(dice, sides)

print(roll)

# source : https://www.youtube.com/watch?v=bsIYU_q5g7Y