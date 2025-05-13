info = {
  "Name":"Gtm Bro",
  "Age":"18",
  "Hobbies":"Coding,Gym",
  567:"Random_key"
}

# print(info[567]) 
# print(info["Yoo"]) #Throws an error
# print(info.get("Yoo")) #Returns none

# print(info.keys())
# print(info.values())

# for i in info.keys():
#   print(f"The corresponding value for {i} is {info[i]}")

for j,k in info.items():
  print(f"The corresponding value for {j} is {k}")
  
