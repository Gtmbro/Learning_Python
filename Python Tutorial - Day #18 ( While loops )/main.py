# print("We are going to give the square of the numbers that you enter:")
# print("But the limit is 1000")
# print()

# i = int(input("Enter the number: "))
# while(i<=1000):
#   print("Square of",i,"is: ",i*i)
#   i = int(input("Enter another number: "))
# # print("Limit exceeded..")
# else:
#   print("Limit exceeded..")

c = int(input("Enter any num & you'll find the nums that are smaller than that:"))
c = c-1
while True:
  print(c)
  c = c-1
  if c<=0:
    break
