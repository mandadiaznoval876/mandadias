import os

old_name = "python_practice_folder"
new_name = "python_practice_folder_new"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("Directory renamed successfully.")
else:
    print("Directory not found.")
