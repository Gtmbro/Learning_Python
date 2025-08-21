import pyttsx3
teller = pyttsx3.init()

people = ["John","Abraham","Will"]

for person in people:
    teller.say(f"Hello {person}")

teller.runAndWait()
