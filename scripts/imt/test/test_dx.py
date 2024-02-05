import os
import shutil
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import convert_now


class TestDeveloperExperience:
  # Variable
  root = "test/"
  input_folder = f"{root}/assets"
  output_folder = f"{root}/export"
  radius = 48
  # Test assets
  literal_test_picture = "test_input.png"
  test_picture = f"{root}/{literal_test_picture}"
  # Assertion
  test_picture_png = os.path.join(output_folder, f"{literal_test_picture.strip('.png')}.png")
  test_picture_webp = os.path.join(output_folder, f"{literal_test_picture.strip('.png')}.webp")

  def test_create_folder(self):
    if os.path.exists(self.input_folder) or os.path.exists(self.output_folder):
      shutil.rmtree(self.input_folder)
      shutil.rmtree(self.output_folder)
    convert_now.setup(self.input_folder, self.output_folder)
    assert os.path.exists(self.input_folder) and os.path.exists(self.output_folder)


  def test_process(self):
    if os.path.exists(self.input_folder) or os.path.exists(self.output_folder):
      shutil.rmtree(self.input_folder)
      shutil.rmtree(self.output_folder)
    convert_now.setup(self.input_folder, self.output_folder)
    shutil.copy(self.test_picture, self.input_folder)
    convert_now.main(self.input_folder, self.output_folder, self.radius)
    assert os.path.exists(self.test_picture_png) and os.path.exists(self.test_picture_webp)

if __name__ == "__main__":
  pytest.main()