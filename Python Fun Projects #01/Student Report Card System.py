import time

students_objs_list = []

#-----------------Student Class---------------------
class Student:
  no_of_students = 0
  
  def __init__(self, name, marks_list):
    if not marks_list:
      raise ValueError("marks_list cannot be empty.")
    if any((m < 0 or m > 100) for m in marks_list):
      raise ValueError("All marks must be between 0 and 100.")
      
    self.name = name
    self._marks_list = marks_list
    self.no_of_subjects = len(marks_list)
    Student.no_of_students += 1

  @staticmethod
  def Sub_gpa(mark):
    # Upper bound inclusive, lower bound exclusive except bottom
    if 90 < mark <= 100:
      return 4.0
    if 80 < mark <= 90:
      return 3.6
    if 70 < mark <= 80:
      return 3.2
    if 60 < mark <= 70:
      return 2.8
    if 50 < mark <= 60:
      return 2.4
    if 40 < mark <= 50:
      return 2.0
    return 0.0

  @property
  def GPA(self):
    return sum(self.Sub_gpa(m) for m in self._marks_list)/self.no_of_subjects 

#-----------------TopperStudent (inherited ) Class---------------------
class TopperStudent(Student):
  """Represents the student who ranked #1 (or tied #1). Adds the ranking and rewards."""
  def __init__(self, base_student, rank = 1, award = None):
  #Using data from existing student
    super().__init__(base_student.name, base_student._marks_list)
    self.rank = rank
    self.award = award

  def show_topper(self):
    print(f"🎉 Topper is: {self.name} | GPA: {self.GPA:.2f} | Rank: {self.rank}")
    if self.award:
      print(f"Award: {self.award}")

def find_toppers(student_objs):
  """Return list of students with highest GPA (and if ties as well)"""
  if not student_objs:
    return []
  gpas = [gpa.GPA for gpa in student_objs]
  max_gpa = max(gpas)

  return [t for t in student_objs if t.GPA == max_gpa]

  
#-----------------------INPUT Section-------------------------------
decision = input("Enter 'y' to give name and marks of the students\n"
                 "Enter anything else to exit: ").strip().lower()

i = 1
while decision == 'y':
  student_name = input(f"\nEnter the name of the student no {i}: ").capitalize()
  student_marks = list(map(float,input("\nEnter the marks of all the subjects"
                                     f" of {student_name}: ").split()))
  try:
     student_obj = Student(student_name, student_marks)
  except ValueError as e:
     print(f" Invalid input: {e}, try this student again.")
     continue
  
  students_objs_list.append(student_obj)

  decision = input("\nEnter 'y' again to give name and marks of the students\n"
                 "Enter anything else to exit: ").strip().lower()
  i += 1


if students_objs_list:
  print("\n"+"="*30)
  print("STUDENTS REPORT CARD")
  print("-"*30)
  print(f"{'Name':<15} {'GPA':<5}")
  print("-"*30)

  for student in students_objs_list:
    print(f"{student.name:<15} {student.GPA:<5.2f}")
    print("-"*30)

  toppers = find_toppers(students_objs_list)
  
  print("="*30)
  print(f"\nTotal number of students is: {Student.no_of_students}")
  print("\nAnd for the final reveal of the topper..")
  print("\nLadies and gentlemen, the topper is:\n")
  time.sleep(2)

  if len(toppers) == 1:
    top = TopperStudent(toppers[0], award="🏆Gold Medal")
    top.show_topper()

  else:
    print("Congratulations for many toppers..\n")
    for rank, std in enumerate(toppers, start=1):
      top = TopperStudent(std, rank=rank, award="🏆Gold Medal")
      top.show_topper()
    
else:
  print("No students have been added.")

