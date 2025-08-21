# For Mac:-

# from os import system

# names = ["Sundar Pichai","Bill Gates","Steve Jobs","Mark Zukerburg","Tim Cook"]

# for name in names:
#   system(f"Shoutout to {name}")

#For Windows:-

from win32com.client import Dispatch

speaker = Dispatch("SAPI.SpVoice")

names = ["Sundar Pichai","Bill Gates","Steve Jobs","Mark Zukerburg","Tim Cook"]
for name in names:
    speaker.speak(f"Shoutout to {name}")
