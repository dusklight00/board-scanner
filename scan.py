from pydoc import Doc
from packages.scanner import DocScanner
import os

scanner = DocScanner(interactive=False)

def scan_folder(folder_path):
    for image_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, image_name)
        scanner.scan(full_path)
        
scan_folder("raw")
