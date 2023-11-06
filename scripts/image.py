import os
from PIL import Image, ImageOps, ImageDraw, ImageFilter

if __name__ == "__main__":
  pass #exit()

def add_margin(
  img:          Image.Image, 
  margin_size:  int
) -> Image.Image:
  """Add margin to the input image.

  #### ⚙️ Args:
    input_file_path: The path of the input image file.
    margin_size: The size of the margin to be added.

  #### ↪️ Returns:
    The image with added margin.
  
  #### 🚧 Raises:
    ValueError: If the margin size is not greater than 0.
  """
  if margin_size <= 0:
    raise ValueError(f"🥞 The margin size must be greater than 0. Got {margin_size}.")

  border = (margin_size, margin_size, margin_size, margin_size)
  img_with_border = ImageOps.expand(img, border=border)
  print(f"🥞 Image size after adding margin: {img_with_border.size}")
  return img_with_border


def round_corners(
  img:            Image.Image, 
  corner_radius:  int
) -> Image.Image:
  """Add rounded corners to the input image.

  #### ⚙️ Args:
    img: The input image.
    corner_radius: The radius of the rounded corners.

  #### ↪️ Returns:
    The image with rounded corners.
  
  #### 🚧 Raises:
    ValueError: If the corner radius is not greater than 0.
  """
  if corner_radius <= 0:
    raise ValueError(f"🥞 The corner radius must be greater than 0. Got {corner_radius}.")
  
  shape_mask = Image.new("L", img.size, 0)
  draw = ImageDraw.Draw(shape_mask)

  draw.rectangle((corner_radius, 0, img.size[0] - corner_radius, img.size[1]), fill=255)
  draw.rectangle((0, corner_radius, img.size[0], img.size[1] - corner_radius), fill=255)
  draw.pieslice(((0.0, 0.0), (corner_radius * 2.0, corner_radius * 2.0)), 180, 270, fill=255)
  draw.pieslice(((img.size[0] - corner_radius * 2.0, 0.0), (img.size[0], corner_radius * 2.0)), 270, 360, fill=255)
  draw.pieslice(((img.size[0] - corner_radius * 2.0, img.size[1] - corner_radius * 2.0), (img.size[0], img.size[1])), 0, 90, fill=255)
  draw.pieslice(((0.0, img.size[1] - corner_radius * 2.0), (corner_radius * 2.0, img.size[1])), 90, 180, fill=255)

  img_mask = Image.new("L", img.size, 255)
  img_mask.paste(shape_mask)
  img_rounded_corners = Image.composite(img.convert("RGBA"), Image.new("RGBA", img.size), img_mask)

  return img_rounded_corners


def add_glow(
  img:          Image.Image,
  glow_color:   tuple = (0, 0, 0),
  max_alpha:    float = 0,
  blur_radius:  int = 10,
  padding:      int = 50,
) -> Image.Image:
  """Add glow effect to the input image.

  #### ⚙️ Args:
    img: The input image.
    glow_color: The color of the glow in RGB format.
    max_alpha: The maximum alpha value of the glow color.
    blur_radius: The radius of the blur effect for the glow.
    padding: The number of pixels to add to each dimension of the image.

  #### ↪️ Returns:
    The image with added glow.
  """
  new_size = (img.size[0] + padding, img.size[1] + padding)

  glow = Image.new("RGBA", new_size)
  draw = ImageDraw.Draw(glow)

  for i in range(padding):
    alpha = int(max_alpha * (1 - i / padding))  # Adjust alpha here
    color = (glow_color[0], glow_color[1], glow_color[2], alpha)
    draw.rectangle((i, i, new_size[0] - i, new_size[1] - i), outline=color)

  glow.paste(img, (int((new_size[0] - img.size[0]) / 2), int((new_size[1] - img.size[1]) / 2)))
  blurred_glow = glow.filter(ImageFilter.GaussianBlur(blur_radius))

  # Hacky stuff to fix the alpha channel pasted on top of the shadow
  background = Image.new("RGBA", blurred_glow.size)
  background.paste(blurred_glow, (0, 0), mask=blurred_glow)
  background.paste(img, (int((new_size[0] - img.size[0]) / 2), int((new_size[1] - img.size[1]) / 2)), mask=img)

  return background


def export_to_webp(
  image:              Image.Image,
  output_file_path:   str = "output.webp",
  format:             str = "WEBP"
  ) -> None:
  """Export the input image in WebP format.

  #### ⚙️ Args:
    image: The input image.
    output_file_path: The path of the output file.
    format: Bitmap format that 
  """
  image.save(output_file_path, format)
  assert os.path.exists(output_file_path)
  print(f"🥞 Image saved to {output_file_path}")
