
class Student:
  SchoolName = "Horizon" #class variable
  
  def __init__(self, name):
    self.marks = 80 #instance variable
    self.nm = name #instance variable

  def ShowDetails(self):
    print(f"The name of the student is: {self.nm} and school name is: {self.SchoolName}")
    print(f"His marks is {self.marks}")
   
std1 = Student("Amrit")
std1.marks = 90 #instance variable
std1.SchoolName = "Stanford" #instance variable
Student.SchoolName = "Hardward" #Class variable, it's changed for all instances
std1.ShowDetails()
# Student.ShowDetails(std1)
std2 = Student("John")
std2.ShowDetails()
