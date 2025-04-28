a = [2,4,1,3,5,8,3]
print(a)
# a.sort() #sort in ascending order
# a.sort(reverse=True) #sort in descending order
# a.append(6) #adds 6 at the end of list
# a.reverse() #reverses the list

# print(a.index(5)) #prints the index of 5 in the list (Can be affected by recent changes in list)
# print(a.count(3)) #counts how many 6 are there in the list (Can be affected by recent changes in list)

# b = a #Creates a reference of a in b ( changes in b will also reflect in a)
# b = a.copy() #Creates a new copy of a in b ( changes in b wont affect a)
# b[1] = 222

# a.insert(2, 999) # Inserts 999 at index 2

c = ["Amrit","idk","Ichchhya"]
# a.extend(c) # Adds c at the end of a
# print(a)

d = a + c # Adds c and a and stores it in d 
print(d)
