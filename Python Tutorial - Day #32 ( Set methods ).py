# a = {1,2,3,4,5}
# b = {2,4,6,8,10}
# print(a.union(b))
# print(a,b)
# b.update(a) # b = b.union(a)
# print(b)

cities = {"Tokyo","Kathmandu","New delhi","Beiging","New york"} #A
cities2 = {"New york","London","Tokyo","Toronto"} #B
# cities3 = cities.intersection(cities2)
# print(cities3)
# cities4 = cities.symmetric_difference(cities2) # (AuB)-(AnB)
# print(cities4)
# cities5 = cities.difference(cities2) # A-B
# print(cities5)
# cities.intersection_update(cities2)
# print(cities)

# print(cities.isdisjoint(cities2)) #Prints True if no elements are common, or else false

city = {"Tokyo","Madrid","New york","London"}
city2 = {"London","Madrid"}
# print(city.issuperset(city2)) #Prints True if all elements of city2 are in city, or else false.
# print(city.issubset(city2)) #Prints True if all elements of city are in city2, or else false.

# city2.add("Kathmandu") #To add only one item
# print(city2)
# city.update({"Kathmandu","Delhi"}) # To add multiple items
# print(city)
# city2.remove("Madrid") #Removes the item and throws error if not present
# print(city2)
# city.discard("Yoooo") #Removes the item and doesn't throw error if not present
# print(city)

# item = city.pop()
# print(city)
# print(item) # Takes out any random element from the set

# del city # Deletes an entire set
# print(city)
# city.clear() #Clears all elements of the set
# print(city)

if "Tokyo" in city:
  print("Tokyo is present")
else:
  print("Tokyo is absent")
