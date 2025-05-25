questions = [
    "1. What is the capital of Norway ?",
    "2. Which planet is known for having the most moons?",
    "3. Who painted the Mona Lisa?",
    "4. What element has the chemical symbol ‘Fe’?",
    "5. In the Marvel Cinematic Universe, what is Thor’s hammer called?"
]
options = [
  "A. Oslo \nB. Copenhagen \nC. Stockholm  \nD. Helsinki\n",
  "A. Saturn \nB. Mars \nC. Venus \nD. Mercury\n",
  "A. Leonardo da Vinci \nB. Pablo Picasso \nC. Vincent van Gogh \nD. Claude Monet\n",
  "A. Fluorine \nB. Francium \nC. Iron \nD. Ferrite\n",
  "A. Stormbreaker \nB. Mjolnir \nC. Excalibur \nD. Gungnir\n"
]

answers = [
  "Oslo",
  "Saturn",
  "Leonardo da Vinci",
  "Iron",
  "Mjolnir"
]

alpha = [
  "A",
  "A",
  "A",
  "C",
  "B"
]

for i in range(5):
  print(questions[i])
  print(options[i])
  user = input()
  if user.strip().lower() == answers[i] or user.strip().upper() == alpha[i]:
    print("Correct")
    print()
