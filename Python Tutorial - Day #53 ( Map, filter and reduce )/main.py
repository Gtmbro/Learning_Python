
from functools import reduce

lol = [1,2,3,4,5,6,7,8,9,10]

top = reduce(lambda b,d: b+d , lol)
print(top)

def sqr(x):
  return x*x
  
nums = list(map(int,input("Enter each item: ").split())) #Takes space separated input from user.

func = list(map(sqr,nums))
print(func)

# def filter_function(x):
#   return x%2==0

new = list(filter(lambda x: x%2==0,nums))
print(new)

