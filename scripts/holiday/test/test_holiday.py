import os
import sys
from datetime import datetime

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import holiday


class TestDynamicSetter:
    def test_holiday_return_event(self):
        datetime_obj = datetime(1337, 2, 14)
        output = holiday.get_current_event(datetime_obj)
        assert output == "valentine"

    def test_holiday_ignore_day(self):
        # Test where the ignore_day flag is set to True and selects the first event in February
        datetime_obj = datetime(1337, 2, 1)  # Not exactly on Valentine's Day
        output = holiday.get_current_event(datetime_obj, ignore_day=True)
        assert output == "valentine"

    def test_holiday_exclude_theme(self):
        # Test exclusion of 'valentine' theme, should return default since no other event on Feb 14
        datetime_obj = datetime(1337, 2, 14)
        output = holiday.get_current_event(datetime_obj, exclude=["valentine"])
        assert output == "default"

    def test_holiday_exclude_multiple(self):
        # Exclude 'valentine', should return 'default' since no other event
        datetime_obj = datetime(1337, 2, 14)
        output = holiday.get_current_event(
            datetime_obj, exclude=["valentine", "newyear"]
        )
        assert output == "default"

    def test_str_input_light(self):
        # Test theme copying for light mode
        os.makedirs("test/testbed_assets", exist_ok=True)
        os.makedirs("test/testbed", exist_ok=True)

        holiday.dynamic_setter(
            theme="default",
            mode="light",
            source_path="test/testbed_assets/",
            destination_path="test/testbed/",
        )
        assert os.path.isfile("test/testbed/dynamic-light.webp")
        os.remove("test/testbed/dynamic-light.webp")

        holiday.dynamic_setter(
            theme="valentine",
            mode="light",
            source_path="test/testbed_assets/",
            destination_path="test/testbed/",
        )
        assert os.path.isfile("test/testbed/dynamic-light.webp")
        os.remove("test/testbed/dynamic-light.webp")

    def test_str_input_dark(self):
        # Test theme copying for dark mode
        os.makedirs("test/testbed_assets", exist_ok=True)
        os.makedirs("test/testbed", exist_ok=True)

        holiday.dynamic_setter(
            theme="default",
            mode="dark",
            source_path="test/testbed_assets/",
            destination_path="test/testbed/",
        )
        assert os.path.isfile("test/testbed/dynamic-dark.webp")
        os.remove("test/testbed/dynamic-dark.webp")

        holiday.dynamic_setter(
            theme="valentine",
            mode="dark",
            source_path="test/testbed_assets/",
            destination_path="test/testbed/",
        )
        assert os.path.isfile("test/testbed/dynamic-dark.webp")
        os.remove("test/testbed/dynamic-dark.webp")

    def test_list_input_lightdark(self):
        # Test theme copying for both light and dark modes
        os.makedirs("test/testbed_assets", exist_ok=True)
        os.makedirs("test/testbed", exist_ok=True)

        holiday.dynamic_setter(
            theme=["default", "valentine"],
            mode=["light", "dark"],
            source_path="test/testbed_assets/",
            destination_path="test/testbed/",
        )
        assert os.path.isfile("test/testbed/dynamic-light.webp")
        assert os.path.isfile("test/testbed/dynamic-dark.webp")
        os.remove("test/testbed/dynamic-light.webp")
        os.remove("test/testbed/dynamic-dark.webp")

    def test_holiday_return_event_with_ignore_and_exclude(self):
        # Test with both ignore_day and exclude functionality combined
        datetime_obj = datetime(1337, 12, 1)
        output = holiday.get_current_event(
            datetime_obj, ignore_day=True, exclude=["newyear"]
        )
        assert output == "default"


if __name__ == "__main__":
    pytest.main()
