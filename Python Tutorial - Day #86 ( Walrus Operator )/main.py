print("."*55 + "Language Logger" + "."*55)

languages = list()
print("Enter 'quit' to quit.")
while (a := input("Enter the language: ")) != "quit": # := walrus operator,which is an expression that can be used in the same line and returns a value.
  languages.append(a)

print(f"Favourite languages: {languages}")
