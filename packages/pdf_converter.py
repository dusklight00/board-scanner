from PIL import Image
import os

def convert_folder_to_pdf(folder_path, output_path):
  image_list = []

  for image_name in os.listdir(folder_path):
    full_path = os.path.join(folder_path, image_name)
    image = Image.open(full_path)
    image = image.convert("RGB")
    image_list.append(image)
  
  first_image = image_list.pop(0)
  first_image.save(output_path, append_images=image_list, save_all=True)