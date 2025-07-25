import os

def rename(format):
  i = 1
  for file in os.listdir():
    if file.endswith(f".{format}") and file != "main.py":
      new_name = f"{i}.{format}"
      if file != new_name:
        os.rename(file,new_name)
        i += 1

input = input("Enter your file format ( for eg: pdf, txt ): ")
output = rename(input)
