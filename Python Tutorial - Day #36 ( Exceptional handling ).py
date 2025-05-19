# a = input("Man.. you gotta enter a number now:\n")
# print(f"Multiplication table of {a} is:\n")

# try:
#   for i in range(1,11):
#     print(f"{a} x {i} = {int(a)*i}")
# except:
#   print(f"How tf do you think '{a}' is a number ??")

b = [1,2,3]
try:
  num = int(input("Enter an integer: "))
  print(b[num])
except ValueError:
  print("It's a value error.")
except IndexError:
  print("It's an index error.")

