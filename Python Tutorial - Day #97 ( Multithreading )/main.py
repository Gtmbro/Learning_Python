import threading
import time
import math

def executer(func, n):
    t = threading.Thread(target=func, args=[n]) #Creates new thread object.
    t.start() #Starts our thread
    print(t) #Prints the thread object
    t.join() #to make it wait till main thread finishes.
    
def sqroot(num):
    time.sleep(2)
    print(math.sqrt(num))

t1 = executer(sqroot, 4)
t2 = executer(sqroot, 9)
