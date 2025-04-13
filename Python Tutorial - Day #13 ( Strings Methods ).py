# Strings are immutable/unchangable
a = "Amrit"
print("1:-")
print(a.upper())
print("2:-")
print(a.lower())
b = a + "iiii"
print("3:-")
print(b)
print("4:-")
print(b.rstrip("i")) #Removes the trailing characters

print("5:-")
print(a.replace("Amrit","Ankit"))

c = a.replace("Amrit","Amrit Is A Good Boy")
print("6:-")
print(c.split(" "))

Mindset = "just Do It mA gUy, understood?"
print("7:-")
print(Mindset.capitalize()) #Capitalizes 1st letter & everything else in lowercase
print("8:-")
print(len(Mindset))
print("9:-")
print(len(Mindset.center(9))) #Makes the length of the string 9 if it's less than 9 otherwise if it's more than 9, then it adds spaces to make it 9, and prints the length of the string.
print("10:-")
print(Mindset.center(19)) #If the length of string is less than 19, it adds spaces to make it 19, otherwise no change.
print("11:-")
print(Mindset.count("u"))

print("12:-")
print(Mindset.startswith("j"))

print("13:-")
print(Mindset.endswith("u"))
print("14:-")
print(Mindset.endswith("y",13,17)) #Checks if the string ends with "y" from index 13 to 17
d = ("abcdefghij")
print("15:-")
print(d.find("e")) #Finds index of e
# print(d.index("k")) #Throws error if e isn't found
print("16:-")

f = ("IdontknowwtfIamdoing")
print("17:-")
print(f.isalnum()) # Prints true if string is made up of alphabets and numbers only, otherwise false(even if there is a space)
print("18:-")
f = ("I dont know wtf I am doing")
print("19:-")
print(f.isalnum())
g = ("Amritgtm444")
print("20:-")
print(g.isalpha()) # Prints true if string is made up of alphabets only, otherwise false(even if there is a space)7print(16:-)
print("21:-")
print(g.islower()) # Prints true if string is made up of lowercase alphabets only, otherwise false 8
h1 = ("My name is... I don't know man..\n")
print("22:-")
print(h1.isprintable())
h2 = ("My name is... I don't know man..")
print("23:-")
print(h2.isprintable())
str1 = "  "
print("24:-")
print(str1.isspace())

str2 = "My name is Ichhh"
print("25:-")
print(str2.istitle())

str2 = "My Name is Ichhh"
print("26:-")
print(str2.istitle())

print("27:-")
print(str2.swapcase()) # Makes uppercase lower and vice versa

print("28:-")
print(str2.title())
