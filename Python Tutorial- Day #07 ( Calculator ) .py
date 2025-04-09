#print(15//6) #Floor division,deletes the fraction part
#print(15%6) #Module operator, returns the remainder
#print(5**3) #Exponential operator, returns 5 to the power 3

#Calculator:-

while True:

  a = int(input("Enter the first number:"))
  b = int(input("Enter the second number:"))
  print()


  def calculator(a,b):
    c = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division: "))
    print()

    if c == 1:
      print("The sum is: ", a+b)

    elif c == 2:
      if a>b:
        print("The difference is: ", a-b)
      elif b>a:
        print("The difference is: ", b-a)

    elif c == 3:
      print("The multiplication is: ", a*b)

    elif c == 4:
      if a>b:
        print("The division is: ", a/b)
      elif a<b:
        print("The division is: ", b/a)

  calculator(a,b)
  print()
  d = int(input("Enter 1 to do it again and 2 to exit:"))
  print()
  if d == 1:
    continue
  elif d == 2:
    break
  elif d!=1 and d!=2:
    e = int(input("Since, you entered wrong number, would you like to:\n1. F off \"Enter 1\" \n2. Do it again \"Enter 2\" "))
    if e == 1 and e!=2:
      print()
      print("Here you go, F off")
      break
    elif e == 2:
      print()
      continue
