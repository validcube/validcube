import os
import sys
from datetime import datetime

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import holiday


class TestDynamicSetter:
  def test_str_input_light(self):
    os.makedirs('test/testbed', exist_ok=True)
    os.makedirs('test/testbed_copy', exist_ok=True)

    holiday.dynamic_setter(theme='default', mode='light', source_path='test/testbed/', destination_path='test/testbed_copy/')
    assert os.path.isfile('test/testbed_copy/dynamic-light.webp')

    holiday.dynamic_setter(theme='valentine', mode='light', source_path='test/testbed/', destination_path='test/testbed_copy/')
    assert os.path.isfile('test/testbed_copy/dynamic-light.webp')


  def test_list_input_lightdark(self):
    os.makedirs('test/testbed', exist_ok=True)
    os.makedirs('test/testbed_copy', exist_ok=True)

    holiday.dynamic_setter(theme=['default', 'valentine'], mode=['light'], source_path='test/testbed/', destination_path='test/testbed_copy/')

    assert os.path.isfile('test/testbed_copy/dynamic-light.webp')
    #assert os.path.isfile('test/testbed_copy/dynamic-dark.webp')


  def test_holiday_return_event(self):
    datetime_obj = datetime(1337, 2, 14)
    output = holiday.main(datetime_obj)

    assert output == 'valentine'



if __name__ == '__main__':
  pytest.main()