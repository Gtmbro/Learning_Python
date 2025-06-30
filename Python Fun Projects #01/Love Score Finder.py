import time
import random

def love_finder():
  print("💘 Calculating your love score 💘")
  for i in range(5):
    print("🫣"*(i))
    time.sleep(1)
  print()

name1, name2 = input("Enter your name and your crush's name: ").strip().split()
name1 = name1.capitalize()
name2 = name2.capitalize()
percentage = random.randint(20,100)

love_finder()

if name1 == "Amrit" and name2 == "Ichchhya":
  print("🥰 Your love score is 100% 🥰\n🫶  Couple made in heaven..🫶")
  for i in range(1,6):
    print("💞"*(i))
    time.sleep(0.2)
else:
  print(f"Your love score is {percentage}%👉👈")
