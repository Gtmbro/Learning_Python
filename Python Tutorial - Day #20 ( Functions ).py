def multi_table(a):
  for i in range(1,x+1):
    print(a, "x",i,"=",a*i)
    
b = float(input("Enter the number whose multiplication table you wanna find: "))
x = int(input("Enter the range upto which you wanna know the multiplication table: "))
multi_table(b)


def arithmetic(a,b,c):
  d = b-a
  print("The difference between them is: ",d)
  n = float(input("Enter the term upto which u wanna find the sum of: "))
  s = (n/2)*(2*a +(n-1)*d)
  print("The sum is: ",s )

a,b,c = map(float,input("Enter first 3 terms of arithmetic sequence,"
                          "separated with spaces: ").split())
arithmetic(a,b,c)
