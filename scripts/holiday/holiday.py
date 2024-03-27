import os
from datetime import datetime

# Format: Month, Day, Assetclass
Event = {
  'NEW_YEAR': (1, 1, 'newyear'),
  'VALENTINE': (2, 14, 'valentine'),
  'APRIL_FOOL': (4, 1, None),
  'SPECIAL': (7, 10, 'valentine'),
  'BIRTHDAY': (10, 29, None),
  'CHRISTMAS': (12, 25, None),
  'BEFORE_NEW_YEAR': (12, 31, 'newyear')
}


def dynamic_setter(theme: str | list[str],
                   mode: str | list[str],
                   source_path: str,
                   destination_path: str) -> int:
  """Copies and overwrites a file based on a dynamic theme and mode.

  #### ⚙️ Args:
    str/list(theme): The theme or variant of the file to be copied.
    str/list(mode): The mode of the file.
    str(source_path): The path to the directory where the source file is located.
    str(destination_path): The path to the directory where the file should be copied.

  #### ↪️ Returns:
    0 if the file was copied and overwritten successfully, 1 otherwise.
  """

  if isinstance(theme, list) and isinstance(mode, list):
    combinations = [(t, m) for t in theme for m in mode]
  else:
    if isinstance(theme, str):
      theme = [theme]
    if isinstance(mode, str):
      mode = [mode]
    combinations = [(t, m) for t in theme for m in mode]

  for theme, mode in combinations:
    source_file = f'{source_path}{theme}-{mode}.webp'
    destination_file = f'{destination_path}dynamic-{mode}.webp'
    try:
      os.unlink(destination_file)
    except FileNotFoundError:
      pass
    try:
      os.link(source_file, destination_file)
      print("🥞 File copied and overwritten successfully.")
    except OSError as e:
      print(f"🔥 Operation {source_file} -> {destination_file}\n"
            f"🔥 File can't be overwritten: {e}")
      return 1

  return 0


def main(time: datetime) -> str:

  """Finds the current event and returns the appropriate theme.

  #### ⚙️ Args:
    datetime(time): Current or specfic time

  #### ↪️ Returns:
    Supported theme's name in string or else "default"
  """
  today = (time.month, time.day)
  found_match = False
  for event_name, event_date in Event.items():
    if event_date[:2] == today:
      print(f"🥞 Today's date matches {event_name}. Asset: {event_date[2]}")
      found_match = True
      value = str(event_date[2])
  if not found_match:
    print("🗿 Nothing eventful here today.")
    value = 'default'

  return value


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='⛅ Dynamically set wallpaper based on date and event.')
  parser.add_argument('-t', '--theme', type=str, nargs='+', default=main(datetime.now()), help='🎨 Theme of the wallpaper to be copied.')
  parser.add_argument('-m', '--mode', type=str, nargs='+', default='light', help='⛅ Mode of the wallpaper to be copied.')
  parser.add_argument('-s', '--source', type=str, default='', help='📂 Path to the directory where the source file is located.')
  parser.add_argument('-d', '--destination', type=str, default='', help='📂 Path to the directory where the file should be copied.')

  args = parser.parse_args()

  if not args.mode:
    parser.print_help()
    exit()

  dynamic_setter(theme=args.theme, mode=args.mode, source_path=args.source, destination_path=args.destination)
