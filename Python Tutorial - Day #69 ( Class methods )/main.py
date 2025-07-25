class Student:
  School = "Horizon"
  def info(self):
    print(f"The school of {self.name} is {self.School}")

  @classmethod
  def change(idk, new_school):
    idk.School = new_school

s1 = Student()
s1.name = "Amrit"
s1.info()
s1.change("Shanti")
s1.info()
