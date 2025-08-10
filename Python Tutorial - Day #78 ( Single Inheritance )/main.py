class Animal:
  def __init__(self, species, sound):
    self.species = species
    self.sound = sound

  def make_sound(self):
    print(f"{self.species} makes {self.sound}")

class Cat(Animal):
  def __init__(self, name, species="Cat", sound="Meow"):
    Animal.__init__(self, species, sound)
    self.name = name

  def make_sound(self):
    print(f"{self.name} is a Cat of species '{self.species}' and it makes '{self.sound}' sound")

a = Cat("Bella")
a.make_sound()
