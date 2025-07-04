# meteorite.py

import json
import traceback
from utils import log


class Meteorite:
    """
    A simple class representing a meteorite with selected fields:
    - id: unique identifier (int)
    - name: meteorite name (string)
    - mass: in grams (float)
    - year: discovery year (int)
    """

    def __init__(self, data):
        try:
            # Extract ID and name, stripping quotes
            self.id = int(data[2][2].replace("'", ''))
            self.name = data[1][2].replace("'", '')

            # Extract mass if the field is correctly structured
            self.mass = 0
            if data[5][1] == "'Mass'" and data[5][2][0] == 'Quantity':
                self.mass = float(data[5][2][1])

            # Extract year if present and correctly structured
            self.year = 0
            if data[7][1] == "'Year'" and data[7][2][0] == 'DateObject':
                self.year = int(data[7][2][1][1])

        except Exception as e:
            # If parsing fails, log detailed traceback for debugging
            log("Parsing error:", traceback.format_exc())
            raise Exception(f"Meteorite parsing failed: {e}")

    def __str__(self):
        return f"<Meteorite \"{self.name}\" Year={self.year} ID={self.id} Mass={self.mass}g>"


def parse_meteorites(file_path, debug=False):
    """
    Load and parse the meteorite dataset from a JSON file.
    Each valid record is converted into a Meteorite object.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        raw = f.read()

        # Workaround for invalid escape sequences in the JSON
        raw = raw.replace('\\', '\\\\')

        # Load JSON content
        data = json.loads(raw)

        # Skip the header row and start from actual entries
        entries = data[1][1:]

    meteorites = []
    for d in entries:
        try:
            meteorites.append(Meteorite(d))
        except Exception:
            continue  # skip malformed entries silently
    return meteorites


def find_summary(meteorites):
    """
    Print:
    1) Total number of parsed meteorites
    2) Name and mass of the heaviest meteorite
    3) Most common year and how many meteorites it includes
    """
    from collections import Counter

    heaviest = max(meteorites, key=lambda m: m.mass)

    # Count occurrences of each year
    years = Counter([m.year for m in meteorites if m.year])

    most_year, freq = years.most_common(1)[0]

    print(f"1) Total entries: {len(meteorites)}")
    print(f"2) Heaviest: {heaviest.name} ({heaviest.mass:,}g)")
    print(f"3) Most frequent year: {most_year} ({freq} entries)")


def find_by_id_or_name(meteorites, id_=None, name=None):
    """
    Search for a meteorite by ID or name.
    Returns the first matching result, or None if not found.
    """
    for m in meteorites:
        if (id_ and m.id == id_) or (name and m.name == name):
            return m
    return None
