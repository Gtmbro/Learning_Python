#main.py:-

import os

if (not os.path.exists("tutorial")):
    os.mkdir("tutorial")

for i in range(1,11):
    os.mkdir(f"tutorial/Day{i}")

#rename.py:-

import os

for i in range(1,11):
    os.rename(f"tutorial/Day{i}",f"tutorial/ Night{i}")

#findlists.py:-

import os

folders = os.listdir("tutorial")

print(folders)

for i in folders:
    print(i)
    print(os.listdir(f"tutorial/{i}"))
