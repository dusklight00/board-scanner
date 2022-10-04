import os

def clean_folder(folder_path):
  for file_name in os.listdir(folder_path):
    full_file_path = os.path.join(folder_path, file_name)
    os.remove(full_file_path)