import os

folder_paths = [
    r'C:\Windows\Temp',
    r'C:\Windows\Prefetch',
    r'C:\Users\ADMIN\AppData\Local\Temp'
]
for folder_path in folder_paths:
    # List all files in the folder
    files = os.listdir(folder_path)
# List all files in the folder
files = os.listdir(folder_path)

# Iterate through the files and delete them
for file in files:
    file_path = os.path.join(folder_path, file)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")
