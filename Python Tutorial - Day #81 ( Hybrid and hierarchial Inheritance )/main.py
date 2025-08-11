
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = int(age)

  def show(self):
    print(f"{self.name} is {self.age} years old.")
    
#Employee-Human (Single inheritance)
class Employee(Human):
  def __init__(self, name, age, company):
    Human.__init__(self, name, age) #Calls constructor of Human.
    self.company = company

  def show(self):
    Human.show(self) #Calls show method of Human.
    print(f"He works in {self.company}.")

#Human-Programmer (Multilevel Inheritance)
class Programmer(Employee):
  def __init__(self, name, age, company, language):
    Employee.__init__(self, name, age, company) #Calls constructor of Employee.
    self.language = language

  def show(self):
    Employee.show(self) #Calls show method of Employee.
    print(f"And he programmes in '{self.language}'.")
    print(f"And when he turns {self.age+1}, he will be promoted.")

person = Programmer("John",20, "Apple", "Python")
person.show()

class Father:
  def __init__(self, father):
    self.father = father

  def show(self):
    return self.father

class Mother:
  def __init__(self, mother):
    self.mother = mother

  def show(self):
    return self.mother

#Son is inherited from Husband and Wife (Multiple Inheritance)
class Son(Father, Mother):
  def __init__(self, father, mother, son1):
    Father.__init__(self, father)
    Mother.__init__(self, mother)
    self.son1 = son1

  def show(self):
    print(f"{self.son1} is the son of Mr.{self.father} and Mrs.{self.mother}.")

print()
child = Son("Alexander","Emily","Alex")
child.show()

#Hybrid Inheritance:- Son2 is inherited from Human(Single inheritance), and Son, which is inherited from Father and Mother (Multiple Inheritance)
class Son2(Human, Son):
  def __init__(self, name, age, father, mother, son1, hobby):
    Human.__init__(self, name, age)
    Son.__init__(self, father, mother, son1)
    self.hobby = hobby

  def show(self):
    Human.show(self)
    print(f"{self.name} is the son of {self.father} and {self.mother}.")
    print(f"He likes to {self.hobby} just like his brother {self.son1}.")

print()
child2 = Son2("Sam",18,"Alexander","Emily","Alex","Coding")
child2.show()
