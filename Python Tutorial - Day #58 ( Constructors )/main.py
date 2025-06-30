
class person:
  def __init__(self, a, b): #__init__():- constructor
    self.name = a
    self.occupation = b

  def info(self):
    print(f"{self.name} is a {self.occupation}")

a = person("Ana","Nan")
b = person("Nan","Ana")
a.info()
b.info()
