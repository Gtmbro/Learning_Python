from win32com.client import Dispatch

speaker = Dispatch("SAPI.SpVoice")

names = ["Sundar Pichai","Bill Gates","Steve Jobs","Mark Zukerburg","Tim Cook"]
for name in names:
    speaker.speak(f"Shoutout to {name}")
