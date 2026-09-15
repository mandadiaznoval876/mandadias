import os

directory = "python_practice_folder"

if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created successfully.")
else:
    print("Directory already exists.")
