# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x is y)   # False, even though values are same
# print(x == y)   # True, because values are same

def get_data_from_user():
  response = input("Enter something or leave blank: ").strip()
  if response == "":
      return None
  return response

data = get_data_from_user()

# if data == "None": checks for the literal string "None"
if data is None:
  print("User gave no input")
else:
  print(data)
