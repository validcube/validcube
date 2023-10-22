import os
import sys
import pytest
from PIL import Image
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import image # noqa: E402

class TestAddMargin:
  input_file_path = "test_input.png"
  img = Image.open(input_file_path)
  # Check if the output image has the correct size

  def test_add_margin_negative(self):
    margin_size = -1
    img = Image.open(self.input_file_path)
    with pytest.raises(ValueError):
      image.add_margin(img, margin_size)


  def test_add_margin_50(self):
    margin_size = 50
    img = Image.open(self.input_file_path)
    img_with_border = image.add_margin(img, margin_size)
    assert img_with_border.size == (
      img.width + 2 * margin_size,
      img.height + 2 * margin_size,
    )

  def test_add_margin_100(self):
    margin_size = 100
    img = Image.open(self.input_file_path)
    img_with_border = image.add_margin(img, margin_size)
    assert img_with_border.size == (
      img.width + 2 * margin_size,
      img.height + 2 * margin_size,
    )
  
  def test_add_margin_1000(self):
    margin_size = 1000
    img = Image.open(self.input_file_path)
    img_with_border = image.add_margin(img, margin_size)
    assert img_with_border.size == (
      img.width + 2 * margin_size,
      img.height + 2 * margin_size,
    )


class TestRoundCorner:
  input_file_path = "test_input.png"
  img = Image.open(input_file_path)
  # Check if the output image has the correct size

  def test_corner_negative(self):
    corner_radius = -1
    with pytest.raises(ValueError):
      image.round_corners(self.img, corner_radius)

  def test_corner_precise(self):
    corner_radius = 0.44322
    img_rounded_corners = image.round_corners(self.img, corner_radius)
    assert img_rounded_corners.size == self.img.size

  def test_corner_8(self):
    corner_radius = 8
    img_rounded_corners = image.round_corners(self.img, corner_radius)
    assert img_rounded_corners.size == self.img.size

  def test_corner_16(self):
    corner_radius = 16
    img_rounded_corners = image.round_corners(self.img, corner_radius)
    assert img_rounded_corners.size == self.img.size

  def test_corner_24(self):
    corner_radius = 24
    img_rounded_corners = image.round_corners(self.img, corner_radius)
    assert img_rounded_corners.size == self.img.size


def test_export_to_webp():
  if os.path.exists("test_output.webp"):
    os.remove("test_output.webp")

  input_file_path = "test_input.png"

  img = Image.open(input_file_path)
  image.export_to_webp(img, "test_output.webp")

  # Check if the output file exists
  assert os.path.exists("test_output.webp")
  os.remove("test_output.webp")


if __name__ == "__main__":
  pytest.main()
