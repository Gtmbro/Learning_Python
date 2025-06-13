sp = "\n"

names = ["Jake","Jenna","Ichchhya","Tyler","Madison"]

for a,i in enumerate(names, start=1):
  # print(f"{a} {i}")
  print(f"{a} {i}") if i!= "Ichchhya" else print(f"{sp}I found you, {i} {sp}")
  # if i == "Ichchhya":
  #   print(f"{sp}I found you, {i} {sp}")
