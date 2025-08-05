class Family:
  def __init__(self, father, mother, son):
    self.father = father
    self.mother = mother
    self.son = son

  def display(self):
    return (f"Father is: {self.father}\nMother is: {self.mother}\nSon is: {self.son}\n")

class Family2(Family):
  def __init__(self, daughter, father, mother, son):
    super().__init__(father, mother, son)
    self.daughter = daughter

  def display(self): #Overrided method of Parent class.
    return (f"Daughter is: {self.daughter}\n" + super().display())

family = Family("John","Amy","Jack")
print(family.display())

family2 = Family2("Ama","Alexander","Amily","Napolean",)
print(family2.display())
