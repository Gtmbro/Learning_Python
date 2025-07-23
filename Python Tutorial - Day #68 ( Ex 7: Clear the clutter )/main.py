
import os

i = 1
for file in os.listdir():
  if file.endswith(".png"):
    new_name = f"{i}.png"
    if file != new_name:
      os.rename(file,new_name)
    i += 1
