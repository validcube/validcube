import os
from datetime import datetime

EVENTS = {
  'NEW_YEAR': (1, 1, 'newyear'),
  'VALENTINE': (2, 14, 'valentine'),
  'APRIL_FOOL': (4, 1, None),
  'SPECIAL': (7, 10, 'valentine'),
  'BIRTHDAY': (10, 29, None),
  'CHRISTMAS': (12, 25, None),
  'BEFORE_NEW_YEAR': (12, 31, 'newyear')
}


def dynamic_setter(theme, mode, source_path, destination_path):
    """Copies and overwrites a file based on dynamic theme and mode.

    Args:
        theme(str | list[str]): The theme(s) of the file to be copied.
        mode(str | list[str]): The mode(s) of the file (e.g., 'light', 'dark').
        source_path(str): The directory path where the source file is located.
        destination_path(str): The directory path where the file should be copied.

    Returns:
        int: 0 if the file was copied and overwritten successfully, 1 otherwise.
    """
    if isinstance(theme, str):
        theme = [theme]
    if isinstance(mode, str):
        mode = [mode]

    for t, m in [(t, m) for t in theme for m in mode]:
        source_file = os.path.join(source_path, f'{t}-{m}.webp')
        destination_file = os.path.join(destination_path, f'dynamic-{m}.webp')

        try:
            os.unlink(destination_file)
        except FileNotFoundError:
            pass

        try:
            os.link(source_file, destination_file)
            print("🥞 File copied and overwritten successfully.")
        except OSError as e:
            print(f"🔥 Failed to copy {source_file} -> {destination_file}: {e}")
            return 1

    return 0


def get_current_event(time, ignore_day=False, exclude=None):
    """Finds the current event based on the date and optional exclusions.

    Args:
        time(datetime): The current or specified time.
        ignore_day(bool): Whether to match events based only on the month, ignoring the day.
        exclude(list[str]): List of themes to exclude.

    Returns:
        str: The name of the event's theme, or 'default' if no event matches.
    """
    today_month = time.month
    today_day = time.day

    if exclude is None:
        exclude = []

    for event_name, event_date in EVENTS.items():
        if event_date[0] == today_month and (ignore_day or event_date[1] == today_day):
            theme = event_date[2] if event_date[2] else "default"
            if theme in exclude:
                print(f"🔥 Skipping excluded theme: {theme}")
                continue
            print(f"🎉 Event found: {event_name}. Asset: {theme}")
            return theme

    print("📅 No matching event.")
    return "default"


def main():
    """Main function that handles argument parsing and runs the dynamic setter."""
    import argparse

    parser = argparse.ArgumentParser(description='⛅ Dynamically set wallpaper based on date and event.')
    parser.add_argument('-t', '--theme', type=str, nargs='+', default=[get_current_event(datetime.now())],
                        help='🎨 Theme(s) of the wallpaper to be copied.')
    parser.add_argument('-m', '--mode', type=str, nargs='+', default=['light'],
                        help='🌗 Mode(s) of the wallpaper to be copied (e.g., light or dark).')
    parser.add_argument('-s', '--source', type=str, required=True,
                        help='📂 Path to the directory where the source file is located.')
    parser.add_argument('-d', '--destination', type=str, required=True,
                        help='📂 Path to the directory where the file should be copied.')
    parser.add_argument('--ignore-day', action='store_true',
                        help='📅 If set, will select an event based only on the month, ignoring the day.')
    parser.add_argument('--exclude', type=str, nargs='+', default=[],
                        help='⛔ Themes to exclude from being used.')

    args = parser.parse_args()

    selected_theme = get_current_event(datetime.now(), ignore_day=args.ignore_day, exclude=args.exclude)

    if args.theme == [None]:
        args.theme = [selected_theme]

    result = dynamic_setter(theme=args.theme, mode=args.mode, source_path=args.source, destination_path=args.destination)
    exit(result)


if __name__ == '__main__':
    main()
