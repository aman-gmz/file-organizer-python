import os
import shutil

folder_path ="C:/Users/HP/Downloads"

files = os.listdir(folder_path)

for file in files:
    file_lower = file.lower()
    source = os.path.join(folder_path, file)

    if file_lower.endswith(".jpg") or file_lower.endswith(".png"):
        os.makedirs(folder_path + "/Images", exist_ok=True)
        shutil.move(source, folder_path + "/Images/" + file)

    elif file_lower.endswith(".pdf"):
        os.makedirs(folder_path + "/Documents", exist_ok=True)
        shutil.move(source, folder_path + "/Documents/" + file)

    elif file_lower.endswith(".mp4"):
        os.makedirs(folder_path + "/Videos", exist_ok=True)
        shutil.move(source, folder_path + "/Videos/" + file)

print("Files organized successfully!")