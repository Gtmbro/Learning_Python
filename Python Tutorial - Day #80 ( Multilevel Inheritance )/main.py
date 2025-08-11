
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = int(age)

  def show(self):
    print(f"{self.name} is {self.age} years old.")

class Employee(Human):
  def __init__(self, name, age, company):
    Human.__init__(self, name, age) #Calls constructor of Human.
    self.company = company

  def show(self):
    Human.show(self) #Calls show method of Human.
    print(f"He works in {self.company}.")

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
