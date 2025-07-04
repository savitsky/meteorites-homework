# utils.py

from datetime import datetime
import pytz


def log(*args):
    """
    Print a timestamped log message to standard output.

    Format: ISO 8601 timestamp in UTC followed by the message.
    Example:
        2025-07-04T14:38:21+0000 Some debug message
    """
    timestamp = datetime.now(tz=pytz.utc).strftime('%Y-%m-%dT%H:%M:%S%z')
    print(timestamp, *args, flush=True)


def debug(*args):
    """
    Conditionally log a debug message if '--debug' was passed
    via command-line arguments. Useful for verbose logging in scripts.
    """
    from sys import argv
    if '--debug' in argv:
        log(*args)
