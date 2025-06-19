
names = ["A","B","C"]

with open('marks.txt','r') as f:
  mark = f.readlines()
  for j,i in enumerate(mark): #j gests index & i gets values.
    m = int(i.split(",")[0])
    m1 = int(i.split(",")[1])
    m2 = int(i.split(",")[2])
    print(f"Marks of {names[j]} in Physics is {m}")
    print(f"Marks of {names[j]} in Chemistry is {m1}")
    print(f"Marks of {names[j]} in Maths is {m2}",end="\n\n")

with open('marks.txt','a') as k:
  lines = ['100','200','300']
  for line in lines:
    k.write(line+'\n')


