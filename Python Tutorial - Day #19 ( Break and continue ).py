print("Printing only even numbers from 1 to 20")

for i in range(1,21):
  if i%2 == 0:
   #print("Skipped",i-1)
    print("Printed",i)
    continue
