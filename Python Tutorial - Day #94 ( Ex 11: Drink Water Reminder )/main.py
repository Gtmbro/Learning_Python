
import os
import shutil
from plyer import notification
import time 

while True:
    for item in os.listdir():
        if item.lower() == "stop.txt": #Create stop.txt to terminate the file.
            print("Reminder has been terminated..")

            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(file)
            exit()
    notification.notify(
        title="Drink Water Reminder",
        message="Drink Water bruh.!!!",
        timeout=10
    )
    time.sleep(7200)
