import os
import shutil

def organize_files(folder_path):
    for name in os.listdir(folder_path):
        src = os.path.join(folder_path, name)

        if not os.path.isfile(src):
            continue

        base, dot, ext = name.rpartition('.')
        ext = ext if base and dot else "NOEXT"
        target_dir = os.path.join(folder_path, ext.upper())

        os.makedirs(target_dir, exist_ok=True)

        dst = os.path.join(target_dir, name)
        if os.path.exists(dst):
            base_name = base if base else name  # NOEXT case
            counter = 1
            while True:
                new_name = f"{base_name} ({counter}).{ext}" if base and ext != "NOEXT" else f"{base_name} ({counter})"
                dst = os.path.join(target_dir, new_name)
                if not os.path.exists(dst):
                    break
                counter += 1

        shutil.move(src, dst)
        print(f"Moved: {name} -> {os.path.relpath(dst, folder_path)}")

if __name__ == "__main__":
    organize_files(r"C:\Users\YourName\Downloads")
