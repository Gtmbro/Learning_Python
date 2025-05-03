#Overall 97/100 but can improve the code to handle invalid inputs and 

questions = ["1. What is the capital of Norway ?",
             "2. Which planet is known for having the most moons?",
             "3. Who painted the Mona Lisa?",
             "4. What element has the chemical symbol ‘Fe’?",
             "5. In the Marvel Cinematic Universe, what is Thor’s hammer called?"]

options = ["A. Stockholm \nB. Copenhagen \nC. Oslo  \nD. Helsinki\n",
           "A. Saturn \nB. Mars \nC. Venus \nD. Mercury\n",
           "A. Leonardo da Vinci \nB. Pablo Picasso \nC. Vincent van Gogh \nD. C laude Monet\n",
           "A. Fluorine \nB. Francium \nC. Iron \nD. Ferrite\n",
           "A. Stormbreaker \nB. Mjolnir \nC. Excalibur \nD. Gungnir\n"
          ]

answers = ["Oslo","Saturn","Leonardo da Vinci","Iron","Mjolnir"]

valid_answers = ["C","A","A","C","B"]


def kbc():
  money = 0
  for i in range(len(questions)):
    print(questions[i])
    user = input(options[i])
    if user.strip().lower() == answers[i].lower() or user.upper() == valid_answers[i]:
      money += 1000
      print("Congratulations! You won",money,end="\n\n")
      # print()
    else:
      print("You lost!",end="\n\n")
      break
  # print()
  print("You can take home",money)

kbc()
  
