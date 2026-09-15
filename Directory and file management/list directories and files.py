import os

print("Files and directories:")

items = os.listdir()

for item in items:
    print(item)
