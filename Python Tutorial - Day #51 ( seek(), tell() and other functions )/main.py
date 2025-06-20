code = """#Unnecessary line 1
# Unnecessary line 2
# Here's the code:-
def avg():
  a = int(input("Enter"))
  b = int(input("Enter"))
  print((a+b)/2)

avg()
"""

with open('new.py','w') as d:
  d.write("#Hello guys.")
  d.truncate(6) #Only shows specified characters.
  
with open('new.py','a') as f:
  f.write("\n\n")
  f.write(code)

with open('new.py','r') as a:
  f = a.readline() #Reads 1st line.
  s = a.readline() #Reads 2nd line.
  t = a.readline() #Reads 3rd line.
  fo = a.readline() #Reads 4th line.
  skip = len(f) + len(s) + len(t) + len(fo)
  a.seek(skip) #Skips the required bytes/characters.
  b = a.read() #Reads specific bytes if specified, if not, reads the remaining content.
  print(b)

  print(a.tell()) #Tells how many bytes are skipped.
