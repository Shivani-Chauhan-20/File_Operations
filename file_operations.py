import os
import shutil

# Check current working directory
print("Current working directory:", os.getcwd())

# 1. Create a new directory
new_dir = 'new_directory'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:
    print(f"Directory '{new_dir}' already exists.")

# Check if the directory exists after creation
print("\nDirectory contents after creation:")
print(os.listdir(os.getcwd()))
