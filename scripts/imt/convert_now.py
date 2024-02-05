import os

from image import export_to_webp, round_corners
from PIL import Image

input_folder = "assets"
output_folder = "export"
radius = 48

def setup(
  input_folder:  str,
  output_folder: str
):
  if not os.path.exists(output_folder):
    print("⚠️ output_folder folder does not exist, creating...")
    os.makedirs(output_folder)
  if not os.path.exists(input_folder):
    print("⚠️ input_folder folder does not exist, creating...")
    os.makedirs(input_folder)

def main(
  input_folder:  str,
  output_folder: str,
  radius:        int
):
  for file in os.listdir(input_folder):
    print(f"🗿 Converting {file}")
    img = Image.open(os.path.join(input_folder, file))
    img_rounded_corners = round_corners(img=img, corner_radius=radius)
    export_to_webp(img_rounded_corners, os.path.join(output_folder, f"{file.strip('.png')}.webp"), "WEBP")
    export_to_webp(img_rounded_corners, os.path.join(output_folder, f"{file.strip('.png')}.png"), "PNG")

setup(input_folder, output_folder)
main(input_folder, output_folder, radius)