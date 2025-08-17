
import time

print("Get ready to do crazy stuff.")
for i in range(1, 5):
    print(i)
    time.sleep(1)

def looper():
  for i in range(1000):
    print(i)

# init1 = time.time()
# looper()
# init2 = time.time()
# print(init2-init1) #Time taken to execute looper function.

time1 = time.localtime()
time = time.strftime("%Y-%m-%d %H:%M:%S",time1)

print(time)
print("Year: ",time1.tm_year) 
print("Month: ",time1.tm_mon) 
print("Day of month: ",time1.tm_wday) 

