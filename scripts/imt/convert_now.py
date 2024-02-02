import os
from PIL import Image
from image import round_corners, export_to_webp

for file in os.listdir("assets"):
  print(f"🗿 Converting {file}")
  img = Image.open(os.path.join("assets", file))
  img_rounded_corners = round_corners(img=img, corner_radius=48)
  export_to_webp(img_rounded_corners, os.path.join("output", f"{file.strip('.png')}.webp"), "WEBP")
  export_to_webp(img_rounded_corners, os.path.join("output", f"{file.strip('.png')}.png"), "PNG")
