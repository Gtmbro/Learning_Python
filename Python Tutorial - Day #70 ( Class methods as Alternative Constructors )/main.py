class Person:
  #Constructor
  def __init__(self, name, age):
    self.name = name
    self.age = int(age)

  #Alternative Constructor
  @classmethod
  def altcons(cls, name, age):
    return (f"{name} is {age} years old.")

  #Alternative Constructor
  @classmethod
  def diff(cls, str):
    result = str.split("-")
    return (f"{result[0]} is {result[1]} years old.")

person1 = Person("Amrit",18)
print(person1.name, person1.age)

person2 = Person.altcons("Amrit",18)
print(person2)

person2 = Person.diff("Amrit-18")
print(person2)


