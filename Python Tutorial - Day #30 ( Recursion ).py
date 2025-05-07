# Recursion is a function of defining itself in it.

# factorial(7)=7*6*5*4*3*2*1
# factorial(1 or 0)=1

# def fucturul(n): #Fucturul = factorial lmao
#   if (n==1 or n==0):
#     return 1
#   else:
#     return n*fucturul(n-1)

# print(fucturul(5))

'''Fibonacci Sequence:-'''
def fibonacci(n):
  f0 = 0
  f1 = 1
  for _ in range(n):
    print(f0, end=" ")
    # f0 = f1
    # f1 = f0+f1 #These 2 lines are wrong

    f0, f1 = f1, f0 + f1

print(fibonacci(10))
