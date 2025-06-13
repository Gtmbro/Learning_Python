class mfError(Exception):
  pass
  
input = input("Enter value between 6 to 10: ")
  
if input.lower() == "quit":
  raise mfError("Mf haha")
  
try:
  a=int(input)
  if a<6 or a>10:
    raise ValueError("Value should be between 6 and 10")

except ValueError as i:
  print(f"{i} caused some error")
