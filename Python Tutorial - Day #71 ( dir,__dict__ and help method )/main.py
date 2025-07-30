class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = int(age)
    self.year = 2025

person = Person("John",18)
# print(dir(person))
# print(help(person))
print(person.__dict__)
