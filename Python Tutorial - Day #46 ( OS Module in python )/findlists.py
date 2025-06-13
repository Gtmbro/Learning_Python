import os

folders = os.listdir("tutorial")

print(folders)

for i in folders:
    print(i)
    print(os.listdir(f"tutorial/{i}"))