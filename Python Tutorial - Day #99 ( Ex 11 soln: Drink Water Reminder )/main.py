import schedule, time
from plyer import notification

def reminder():
    notification.notify(
        title="Drink Water Reminder",
        message="Brotha, drink some water..",
        timeout=0
    )

schedule.every(5).seconds.do(reminder)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    time.sleep(1)
    print("Exiting..")
