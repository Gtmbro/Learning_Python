a = "Here you can vote for your favourite programming language"
print(a.center(len(a)*2,"-"))

x = int(input("Enter 1 for Java\nEnter 2 for C++\nEnter 3 for Python\nEnter 4 for Javascript\nEnter 5 for C#:\n\n"))

match x:
  case 1:
    print("OMG, Java lover, huh?")
  case 2:
    print("OMG, C++ lover, huh?")
  case 3:
    print("Yo! My guy is a Python lover, let's go.. ")
  case 4:
    print("OMG, Javascript lover, huh?")
  case 5:
    print("OMG, C# lover, huh?")
  case _:
    print("You should have voted for one at least..")

  
