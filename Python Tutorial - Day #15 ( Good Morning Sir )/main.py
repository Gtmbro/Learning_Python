import time
timestamp1 = time.strftime("%Y:%m:%d:%A:%B") #%Y=YEAR, %m=MONTH, %d=day, %A= day of the week, %B= month of the year
timestamp2 = time.strftime("%H:%M:%S") #%H=HOUR, %M=MINUTE, %S=SECOND

print(timestamp1) # Format: YYYY:MM:DD
print(timestamp2) # Format: HH:MM:SS
print()

if "5:00:00">=timestamp2<"12:00:00":
  print("Good Morning brotha! ")
  
elif "12:00:00">=timestamp2<"17:00:00":
  print("Good Afternoon brotha! ")
  
elif "17:00:00">=timestamp2<"21:00:00":
  print("Good Evening brotha! ")
  
elif "21:00:00">=timestamp2<"5:00:00":
  print("Good Night brotha! ")
  

  
