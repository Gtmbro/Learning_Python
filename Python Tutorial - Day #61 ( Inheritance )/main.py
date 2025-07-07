class Father:
  def __init__(self, name, occupation):
    self.name = name
    self.occupation = occupation

  def Details(self):
    print(f"Hi! I am {self.name}, a {self.occupation}")

class Son(Father):
  def __init__(self, name, occupation, son_name, son_occupation):
    super().__init__(name, occupation)
    self.son_name = son_name
    self.son_occupation = son_occupation

  def Info(self):
    print(f"Hello! I am {self.son_name}, {self.name}'s Son")
    print(f"My Father is a {self.occupation} and I am a {self.son_occupation}")

f = Father("Tom","Doctor")
f.Details()

s = Son("Tom", "Doctor", "John", "Engineer")
s.Info()
