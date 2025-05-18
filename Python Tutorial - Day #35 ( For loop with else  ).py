# for i in range(5):
#   print(i)
#   if i == 3:
#     break
# else:
#   print("Loop has been ended successfully")

# i = 0
# while i < 5:
#   print(i)
#   if i == 3:
#     break
#   i = i + 1
# else:
#   print("Loop has ended")

for k in range(5):
  print("{} is printed in this step.".format(k+1))
  if k+1 == 4:
    print("Loop has been broken here..")
    break
  
else:
  print("All the items of loop are printed successfully.")
