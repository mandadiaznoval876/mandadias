import os

# Membuat file contoh terlebih dahulu
file_name = "example.txt"

with open(file_name, "w") as file:
    file.write("This is an example file.")

# Menghapus file
if os.path.exists(file_name):
    os.remove(file_name)
    print("File removed successfully.")
else:
    print("File not found.")

# Menghapus directory kosong
directory = "python_practice_folder_new"

if os.path.exists(directory):
    os.rmdir(directory)
    print("Directory removed successfully.")
else:
    print("Directory not found.")
