from datetime import datetime


# Format: Month, Day, Asset
class Event:
  NEW_YEAR = 1, 1, None
  VALENTINE = 2, 14, 'valentine'
  APRIL_FOOL = 4, 1, None
  SPECIAL = 7, 10, 'valentine'
  BIRTHDAY = 10, 29, None
  CHRISTMAS = 12, 25, None
  BEFORE_NEW_YEAR = 12, 31, None


def main():
  today = datetime.today()
  found_match = False

  for event_name in dir(Event):
    if event_name.startswith('__'):
      continue

    event = getattr(Event, event_name)
    if isinstance(event, tuple):
      if event[0] == today.month and event[1] == today.day:
        print(f"🥞 Today's date matches {event_name}. Asset: {event[2]}")
        found_match = True
        return event[2]

  if not found_match:
    print("🗿 Nothing eventful here today.")
    return None

main()
