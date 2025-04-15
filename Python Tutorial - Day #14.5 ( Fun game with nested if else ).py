a = "YOU ARE TRAPPED IN A DUNGEON!!"
print(a.center(500))

b = "You have to make decisions to: \n1. Stay Alive \n2. Escape \n3. Die hilariously \n"
print(b)

def game(c):
  c = input("There are 2 tunnels in front of you A and B.\nChoose any one to proceed:\n")

  if c.upper()=="A":
    print("You hear growling… a monster appears")
    print()
    d = int(input("Do you wanna fight it or run ?\nEnter 1 to fight and 0 to run:\n"))
    print()
    if d==1:
      print("Finds a ladder behind the monster → escapes the dungeon = WIN")
      print("Congrats! You made it out alive!")
    elif d==0:
      print("You run, but trip and gets eaten → death ending")
      print("No worries, Better luck next time bro!")
    else:
      print("Invalid input → death ending")
      print("I had told you to choose either 1 or 0 :)\n You are dead now!")

  elif c.upper()=="B":
    print("You find a mysterious old man holding a key")
    e = int(input("Enter 1 if you trust him\nEnter 2 if you wanna ignore him: "))
    if e==1:
      print("He gives you a key to a hidden door\nYou unlock it → find treasure and escapes→ treasure ending")
      print("You found the treasure huh? Congrats!")
    elif e==2:
      print("You walk ahead, fall into a trap → death ending")
      print("Better luck next time bro!")

game("result") #Stores value of c in "result" and calls the function 
