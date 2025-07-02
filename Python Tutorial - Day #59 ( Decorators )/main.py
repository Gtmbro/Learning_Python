def greet(f): 
  def greeting(*args,**kwargs):
    print("Good Morning")
    f(*args,**kwargs)
    print("Hey buddy")
  return greeting # returns the result of greeting to greet.


@greet #sends the function factorial to greet to run
def factorial(n):
  a = 1
  for i in range(1,n):
    a *= (n-i)
  print(n*a)

def sum(a,b):
  print(a+b)

sum(1,2)
factorial(5)

