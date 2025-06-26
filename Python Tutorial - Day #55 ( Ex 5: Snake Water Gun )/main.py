
import random

options = ["Snake","Water","Gun","Snake","Water","Gun","Snake","Water","Gun"]

superior = {"Water":"Gun",
         "Snake":"Water",
         "Gun":"Snake"}

def game():
  if user == comp:
    return "Draw!"
  elif superior[user] == comp:
    return "You Win!"
  else:
    return "You Lose!"

comp = random.choice(options)
user = input("Enter your choice:\nSnake\nWater\nGun\n\n").strip().capitalize()

final = game()
print(final)
