print("."*55 + "Language Logger" + "."*55)

languages = []
print("Enter 'quit' to quit.",end="\n\n")
while (a := input("Enter the language: ")) != "quit": # := walrus operator,which is an expression that can be used in the same line and returns a value.
  languages.append(a)

print(f"Favourite languages: {languages}")
