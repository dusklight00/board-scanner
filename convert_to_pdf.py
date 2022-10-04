import sys
sys.path.append("../")

from packages.pdf_converter import convert_folder_to_pdf

OUTPUT_FOLDER_PATH = "output"
PDF_NAME = "output.pdf"

convert_folder_to_pdf(OUTPUT_FOLDER_PATH, PDF_NAME)