# Python Directory and Files Management
# Semua operasi dilakukan pada folder latihan khusus.

import os
import shutil

print("=== PYTHON DIRECTORY AND FILES MANAGEMENT ===")

# Folder latihan khusus
base_dir = os.path.join(os.getcwd(), "python_file_practice")
os.makedirs(base_dir, exist_ok=True)

print("\nFolder latihan:", base_dir)

# 1. Get Current Directory
print("\n1. GET CURRENT DIRECTORY")
print("Folder kerja saat ini:", os.getcwd())

# 2. Changing Directory
print("\n2. CHANGING DIRECTORY")
old_directory = os.getcwd()
os.chdir(base_dir)
print("Setelah berpindah ke:", os.getcwd())

# 3. List Directories and Files
print("\n3. LIST DIRECTORIES AND FILES")

sample_file = os.path.join(base_dir, "contoh.txt")
with open(sample_file, "w", encoding="utf-8") as file:
    file.write("Ini adalah file latihan Python.\n")

sample_folder = os.path.join(base_dir, "folder_contoh")
os.makedirs(sample_folder, exist_ok=True)

print("Isi folder latihan:")
for item in os.listdir(base_dir):
    print("-", item)

# 4. Making a New Directory
print("\n4. MAKING A NEW DIRECTORY")
new_directory = os.path.join(base_dir, "folder_baru")

if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print("Folder baru berhasil dibuat.")
else:
    print("Folder baru sudah ada.")

# 5. Renaming a Directory or a File
print("\n5. RENAMING A DIRECTORY OR A FILE")

old_file_name = os.path.join(base_dir, "contoh.txt")
new_file_name = os.path.join(base_dir, "contoh_diubah.txt")

if os.path.exists(old_file_name):
    os.rename(old_file_name, new_file_name)
    print("File berhasil diubah namanya.")
else:
    print("File lama tidak ditemukan.")

old_folder_name = os.path.join(base_dir, "folder_contoh")
new_folder_name = os.path.join(base_dir, "folder_diubah")

if os.path.exists(old_folder_name):
    os.rename(old_folder_name, new_folder_name)
    print("Folder berhasil diubah namanya.")
else:
    print("Folder lama tidak ditemukan.")

# 6. Removing Directory or File
print("\n6. REMOVING DIRECTORY OR FILE")

if os.path.exists(new_file_name):
    os.remove(new_file_name)
    print("File latihan berhasil dihapus.")

if os.path.exists(new_directory) and not os.listdir(new_directory):
    os.rmdir(new_directory)
    print("Folder kosong berhasil dihapus.")

# Hanya menghapus folder latihan yang dibuat oleh program ini
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
    print("Folder latihan berhasil dibersihkan.")

# Mengembalikan folder kerja semula
os.chdir(old_directory)
print("\nFolder kerja dikembalikan ke:", os.getcwd())

print("\nPraktik selesai dengan aman.")
