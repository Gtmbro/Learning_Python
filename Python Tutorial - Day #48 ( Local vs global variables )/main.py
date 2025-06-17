a = "Hey" #Global Variable

def bro():
  global a #Global variable is modified
  a = "Hi" 
  y = "Hello" #Local Variable
  print(y)

bro()
print(a)
