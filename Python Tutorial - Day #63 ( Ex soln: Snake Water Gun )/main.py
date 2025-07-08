
import random

choices = ["Snake","Water","Gun"]
comp = random.choice(choices) #choice for a single item

user = int(input("Enter 1 for Snake\nEnter 2 for water\nEnter 3 for gun: "))

try:
  if user == 1:
    user_choice = "Snake"
  elif user == 2:
    user_choice = "Water"
  elif user == 3:
    user_choice = "Gun"
  else:
    print("Please enter from options!")
    exit()

except ValueError:
  print("Invalid input.!")
  exit()
  
superior = {
  "Snake":"Water",
  "Water":"Gun",
  "Gun":"Snake"
}

def game(user_choice, comp_choice):
  if user_choice == comp_choice:
    return"Draw!"
  elif superior[user_choice] == comp_choice:
    return"You Won!"
  else:
    return "You Lost!"

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {comp}")
print(game(user_choice, comp))
