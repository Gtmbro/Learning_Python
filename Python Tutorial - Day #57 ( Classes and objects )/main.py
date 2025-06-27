
class add_exercise:
  name= ""
  sets = 0
  reps = 0
  weight = 0
  def volume(self):
    return f"Your total volume for {self.name} is {self.sets*self.reps*self.weight}kg."

a = add_exercise()

a.name = input("Enter the exercise: ").capitalize()
a.sets = int(input("Enter the sets: "))
a.reps = int(input("Enter the reps: "))
a.weight = int(input("Enter the weight in kg: "))

print(a.volume())
