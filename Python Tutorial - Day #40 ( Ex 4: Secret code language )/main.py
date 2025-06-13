word = input("Enter the word:\n")
print()

def code():
  if len(word)<=3:
    reverse = word[::-1]
    print (reverse)

  else:
    print("Note: If entered letters are more than 3",
    "then only first 3 letters would be acccepted.\n")
          
    # random, random2 = input("Enter any 3 random letters for starting and ending:\n").split()
    random = input("Enter any 3 random letters for starting:\n")
    random2 = input("Enter any 3 random letters for ending:\n")

    random, random2 = random[:3], random2[:3]
    
    word2 = word[1::1]
    word3 = word[0]
    notreverse = random+word2+word3+random2
    print (notreverse)


def decode():
  if len(word)<=6:
    reverse2 = word[::-1] 
    print (reverse2)

  else:
    word4 = word[3:-3:1]
    word5 = word4[-1] + word4[:-1]

    print (word5)




while True:
  try:
    inp = int(input("Enter 1 to code and 2 to decode:\n"))
    if inp == 1:
      code()
      break
    elif inp == 2:
      decode()
      break

  except ValueError:
    print("Invalid input!")
    continue
