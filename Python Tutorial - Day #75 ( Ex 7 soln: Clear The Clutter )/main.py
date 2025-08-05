import os

def splitter(file,index):
 return os.path.splitext(file)[index]

i = 1
for file in os.listdir():
  if splitter(file,1) == ".txt" or splitter(file,1) == ".jpeg" or splitter(file,1) == ".png":
    new_name = f"{os.path.splitext(file)[0]}{i}.{os.path.splitext(file)[1]}"
    if file != new_name:
      os.rename(file,new_name)
    i += 1
