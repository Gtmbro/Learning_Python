import random

def number_war():
  print("\nLet's compare some numbers..")
  comp = random.randint(1,100)
  while True:
    user = yield f"\nComp has chosen: {comp}"
    if user is None:
      continue
    yield f"\nComp: {comp}\nYou: {user}\nHigher: {max(comp, user)}"

    comp = random.randint(1,100)

gen = number_war()

print(next(gen))
print(gen.send(10))

print(next(gen))
print(gen.send(20))
