import time

yup = time.strftime('%H:%M:%S')
print(yup)
# hour = time.strftime('%H')
hour = int(input("Enter your time in hour: \n"))
print(hour)

if 5<=hour<12:
  print("Good Morning Sir")

elif 12<=hour<17:
  print("Good Afternoon Sir")

elif 17<=hour<21:
  print("Good Evening Sir")

else:
  print("Good Night Sir")
