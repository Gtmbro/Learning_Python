import time

questions = [
    "1. What is the capital of Norway ?",
    "2. Which planet is known for having the most moons?",
    "3. Who painted the Mona Lisa?",
    "4. What element has the chemical symbol ‘Fe’?",
    "5. In the Marvel Cinematic Universe, what is Thor’s hammer called?",
    "6. What is the smallest prime number?",
    "7. Who was the first person to walk on the Moon?",
    "8. In which year did India gain independence?",
    "9. Which gas do plants absorb during photosynthesis?",
    "10. What is the square root of 144?"
]
options = [
  "A. Oslo \nB. Copenhagen \nC. Stockholm  \nD. Helsinki",
  "A. Saturn \nB. Mars \nC. Venus \nD. Mercury",
  "A. Leonardo da Vinci \nB. Pablo Picasso \nC. Vincent van Gogh \nD. Claude Monet",
  "A. Fluorine \nB. Francium \nC. Iron \nD. Ferrite",
  "A. Stormbreaker \nB. Mjolnir \nC. Excalibur \nD. Gungnir",
  "A. 0 \nB. 1 \nC. 2 \nD. 3",
  "A. Buzz Aldrin \nB. Neil Armstrong \nC. Yuri Gagarin \nD. Michael Collins",
  "A. 1942 \nB. 1950 \nC. 1945 \nD. 1947",
  "A. Nitrogen \nB. Carbon Dioxide \nC. Oxygen \nD. Hydrogen",
  "A. 10 \nB. 11 \nC. 12 \nD. 13"
]

answers = [
  "Oslo",
  "Saturn",
  "Leonardo da Vinci",
  "Iron",
  "Mjolnir",
  "2",
  "Neil Armstrong",
  "1947",
  "Carbon Dioxide",
  "12"
]

alpha = [
  "A",
  "A",
  "A",
  "C",
  "B",
  "C",
  "B",
  "D",
  "B",
  "C"
]

money = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]


def kbc ():
  print("🎉 Welcome to KBC - Kaun Banega Codepathi! 🎉\n")
  prize = 0

  for i in range(10):
    user = input(f"Question for {money[i]}:-\n{questions[i]}\n{options[i]}\n")

    if user.strip().title() == answers[i] or user.strip().upper() == alpha[i]:
      print(f"✅ Correct! You won Rs.{money[i]} 🎉\n\n")
      time.sleep(1.5)
      prize = money[i]
    else:
      print(f"❌ Wrong! The correct answer was: {answers[i].title()}\n\n")
      break

  print("\n🎯 Game Over!")

  if prize > 0:
    print()
    print(f"🏆 You walk away with Rs.{prize}!") 
  else:
    print()
    print("😓 You didn't win anything this time. Better luck next time!")


kbc()
