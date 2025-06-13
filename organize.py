import os

for file in os.listdir():
  if file.endswith(".py") and file != "organize.py":
    folder = file[:-3]
    os.mkdir(folder)
    with open(file,"r") as a:
      code = a.read()
    with open(f"{folder}/main.py","w") as a:
      a.write(code)
      os.remove(file)
        
