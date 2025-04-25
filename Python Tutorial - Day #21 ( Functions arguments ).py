def names(fname,mname,lname):
  print("Hello",fname,mname,lname+".")

def age(a,b=1):
  print("Oh! so you are",a,"years old huh?")
  print("In",b,"years, you would be",a+b,"years old.")
  
fname,mname,lname = input("Enter your name: ").split()
a = int(input("Enter your age: "))

names(fname,mname,lname)
age(a)

def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  return (sum/len(numbers))
  
c = average(1,2,3)
print(c)

def names(**name):
  print("Hello",name["fname"],name["mname"],name["lname"]+".")

fname,mname,lname = input("Enter your name: ").split()

names(fname=fname,mname=mname,lname=lname)
