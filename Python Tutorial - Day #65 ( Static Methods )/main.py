
class GymMath:
  def __init__(self, weight, reps):
    self.weight = weight
    self.reps = reps
    
  @property
  def pr(self):
    return self.weight*(1+(self.reps/30))

  def goal(self):
    return (self.weight+10)*(1+self.reps/30)
  
  @staticmethod
  def user(x):
    a,b = input("Enter weight and reps: ").split(" ")
    a = float(a)
    b = float(b)
    print(x)
    return a,b

  @staticmethod
  def converter(a, input_kg):
    # kg = lbs/2.2
    # lbs = kg*2.2
    if input_kg:
      kg = a
      lbs = a*2.2
    else:
      lbs = a
      kg = a/2.2
    
    return kg, lbs

statement = ("\nStrong Man...")
x,y = GymMath.user(statement)

user = int(input("Enter 1 if it's in kgs and 2 if it's in pounds."))
input_kg = (user == 1)
# if user != 1 or user != 2:
#   raise ValueError("Error.!!")

weight_kg, weight_lbs = GymMath.converter(x,input_kg)

my_pr = GymMath(weight_kg, y)

pr_kg = my_pr.pr
pr_lbs = pr_kg*2.2

goal_kg = my_pr.goal()
goal_lbs = goal_kg*2.2

print(f"\nYour PR is:{pr_kg:.2f}kgs/{pr_lbs:.2f}lbs.")
print(f"\nYour goal PR for the next year is: {goal_kg:.2f}kgs/{goal_lbs:.2f} lbs.")
