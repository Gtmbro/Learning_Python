
class Father:
  def __init__(self, father_name, surname):
    self.father_name = father_name
    self.surname = surname
  def info(self):
    print(f"I am {self.father_name} {self.surname}.")

class Son(Father):
  def __init__(self, name, father_name, surname):
    super().__init__(father_name, surname)
    self.name = name
  def info(self):
    print(f"I am {self.name} {self.surname}, {self.father_name} {self.surname}'s son.")


father = Father("George","Bush")
son = Son("John","George","Bush")
father.info()
son.info()
