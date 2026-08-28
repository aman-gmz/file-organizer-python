import os
import shutil

folder_path = input("Enter the folder path: ").strip()

if not os.path.exists(folder_path):
    print("Folder not found!")
    exit()

files = os.listdir(folder_path)

for file in files:
    source = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(source):
        continue

    file_lower = file.lower()

    if file_lower.endswith((".jpg", ".jpeg", ".png", ".gif")):
        folder = "Images"

    elif file_lower.endswith((".pdf", ".docx", ".doc", ".txt")):
        folder = "Documents"

    elif file_lower.endswith((".mp4", ".mkv", ".avi", ".mov")):
        folder = "Videos"

    else:
        folder = "Others"

    destination_folder = os.path.join(folder_path, folder)
    os.makedirs(destination_folder, exist_ok=True)

    shutil.move(source, os.path.join(destination_folder, file))

    print(f"Moved: {file} -> {folder}")

print("\nFiles organized successfully!")