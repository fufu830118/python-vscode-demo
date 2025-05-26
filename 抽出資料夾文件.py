import os
import shutil

# 要處理的根目錄
root_dir = r"C:\Users\11405623\Downloads\OneDrive_2025-05-26\ISO 程序書修改"
excluded_folder = "ISO程序書修改-Bernie"

# 遍歷所有子資料夾與檔案
for dirpath, dirnames, filenames in os.walk(root_dir):
    # 忽略指定資料夾
    if excluded_folder in dirpath:
        continue

    for file in filenames:
        if file.lower().endswith(('.docx', '.doc')):
            full_path = os.path.join(dirpath, file)
            destination_path = os.path.join(root_dir, file)

            # 如檔名重複，自動改名避免覆蓋
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(destination_path):
                new_name = f"{base}_{counter}{ext}"
                destination_path = os.path.join(root_dir, new_name)
                counter += 1

            shutil.copy2(full_path, destination_path)
            print(f"✔ 已複製：{full_path} → {destination_path}")
