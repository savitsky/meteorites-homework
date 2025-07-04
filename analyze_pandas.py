#!/usr/bin/env python3
# analyze_pandas.py

import pandas as pd
import json


def analyze_with_pandas(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        raw = f.read().replace('\\', '\\\\')
        data = json.loads(raw)
        rows = data[1][1:]  # skip header

    # Parse each meteorite record and extract selected fields:
    # - id: unique identifier (converted from string to int)
    # - name: meteorite name (stripped of quotes)
    # - mass: mass in grams (as float, or 0 if missing or malformed)
    # - year: discovery year (as int, or 0 if missing)
    # Only well-structured records with at least 8 fields are processed
    df = pd.DataFrame([
        {
            "id": int(row[2][2].replace("'", '')),
            "name": row[1][2].replace("'", ''),
            "mass": float(row[5][2][1]) if row[5][1] == "'Mass'" and isinstance(row[5][2][1], (int, float)) else 0,
            "year": int(row[7][2][1][1]) if row[7][1] == "'Year'" and isinstance(row[7][2][1][1], int) else 0
        }
        for row in rows if isinstance(row, list) and len(row) >= 8
    ])

    # Print results
    print(f"1) Total entries: {len(df)}")

    heaviest = df.loc[df['mass'].idxmax()]
    print(f"2) Heaviest: {heaviest['name']} ({heaviest['mass']:,}g)")

    most_year = df['year'].value_counts().idxmax()
    most_freq = df['year'].value_counts().max()
    print(f"3) Most frequent year: {most_year} ({most_freq} entries)")


if __name__ == "__main__":
    analyze_with_pandas("Meteorite-Landings.json")
