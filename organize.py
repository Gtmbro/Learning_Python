import os
import shutil

def convert_all_to_main_py(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith('.') or filename == "organize.py":
            continue

        # Get name without extension
        name_no_ext, ext = os.path.splitext(filename)

        # Only work with .py files
        if ext != ".py":
            continue

        # Create new folder
        folder_path = os.path.join(directory, name_no_ext)
        os.makedirs(folder_path, exist_ok=True)

        # Set new file path as main.py
        new_file_path = os.path.join(folder_path, "main.py")

        # Move and rename
        shutil.move(file_path, new_file_path)
        print(f"{filename} → {new_file_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    convert_all_to_main_py(base_dir)
