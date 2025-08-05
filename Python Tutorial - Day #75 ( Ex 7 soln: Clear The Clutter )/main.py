import os

def splitter(file,index):
 return os.path.splitext(file)[index]

def cleaner(format):
  i = 1
  for file in os.listdir():
    if splitter(file,1) == f".{format}":
      new_name = f"{i}.{splitter(file,1)}"
      if file != new_name:
        os.rename(file, new_name)
      i += 1

format = input("Enter your format (eg: png, txt, jpeg):\n")
cleaner(format)

decision = input("Enter 1 to do it again:\n")

while decision == "1":
  format = input("Enter your format (eg: png, txt, jpeg):\n")
  cleaner(format)
