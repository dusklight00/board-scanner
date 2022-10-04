import sys
sys.path.append("..")

from packages.scanner import scan_folder

RAW_FOLDER_PATH = "raw"

scan_folder(RAW_FOLDER_PATH)
