class Father:
  def __init__(self, father):
    self.father = father

  def show(self):
    return(f"Father is: {self.father}")

class Mother:
  def __init__(self, mother):
    self.mother = mother

  def show(self):
    return(f"Mother is: {self.mother}")

class Family(Father, Mother): #Class family inherited Father and Mother classes.
  def __init__(self, father, mother, son):
    self.father = father
    self.mother = mother
    self.son = son

  def show(self):
    print(f"{Father.show(self)}\n{Mother.show(self)}\nAnd son is: {self.son}")

home = Family("John","Lia","Alex")
home.show()
