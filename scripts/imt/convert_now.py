import os
from PIL import Image
from image import round_corners, export_to_webp

input_folder = "input"
output_folder = "output"
radius = 48

if not os.path.exists(output_folder):
  os.makedirs(output_folder)
if not os.path.exists(input_folder):
  os.makedirs(input_folder)

for file in os.listdir(input_folder):
  print(f"🗿 Converting {file}")
  img = Image.open(os.path.join(input_folder, file))
  img_rounded_corners = round_corners(img=img, corner_radius=radius)
  export_to_webp(img_rounded_corners, os.path.join(output_folder, f"{file.strip('.png')}.webp"), "WEBP")
  export_to_webp(img_rounded_corners, os.path.join(output_folder, f"{file.strip('.png')}.png"), "PNG")
