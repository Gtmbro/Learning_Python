import requests

# # response = requests.get("https://www.google.com/")

# data = {"name": "Amrit", "power": "Gym & Python"}
# response = requests.post("https://httpbin.org/post", data=data)

# # print(response.status_code)
# # print(response.text)
# print(response.json())

#To get live weather data:-
city = input("Enter the city name: ").capitalize()
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()

print("Current Temp\nIn °C:",data["current_condition"][0]["temp_C"],"°C")
print("In °F:",data["current_condition"][0]["temp_F"],"°F")

