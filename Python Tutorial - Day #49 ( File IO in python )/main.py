text = [
  "This file is for explaining what is happening in the code.\n",
  "This will be explained as the code becomes more complex."
]

with open('explain.txt','w') as a:
  # a.write(text) If the variable doesn't have any list.
  a.writelines(text) # If the variable has a list

# with open('explain.txt','r') as b:
#   item = b.read()
#   print(item)

# with open('explain.txt','a') as c:
#   appended = c.write("\nThis is the appended text.")
#   print(appended)