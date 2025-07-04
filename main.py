#!/usr/bin/env python3

# IDE: PyCharm 2025.1.2 (Community Edition)
# Interpreter: Python 3.10
# Author: devops.vinnyk@gmail.com
# Date: 2025-07-04
# main.py

# Import necessary modules and helper functions
import argparse
from meteorite import parse_meteorites, find_summary, find_by_id_or_name
from analyze_pandas import analyze_with_pandas
from utils import log, debug

# Entry point for the script
if __name__ == '__main__':
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description='Earth Meteorite Landings Analysis')
    parser.add_argument('--file', type=str, default='Meteorite-Landings.json', help='Path to JSON file')
    parser.add_argument('--search-id', type=int, help='Search meteorite by ID')
    parser.add_argument('--search-name', type=str, help='Search meteorite by name')
    parser.add_argument('--print-all', action='store_true', help='Print all parsed meteorites')
    parser.add_argument('--use-pandas', action='store_true', help='Use pandas-based analysis')
    parser.add_argument('--debug', action='store_true', help='Print debug information')
    args = parser.parse_args()

    # Use the pandas-based analysis path if specified
    if args.use_pandas:
        analyze_with_pandas(args.file)
    else:
        # Otherwise use the custom parser to load meteorite data
        meteorites = parse_meteorites(args.file, args.debug)

        # Print all entries if requested
        if args.print_all:
            for m in meteorites:
                print(m)

        # Search for a specific meteorite by ID or name
        elif args.search_id or args.search_name:
            result = find_by_id_or_name(meteorites, id_=args.search_id, name=args.search_name)
            if result:
                print(result)
            else:
                print("Meteorite not found.")

        # Otherwise show general dataset summary (total, heaviest, most frequent year)
        else:
            find_summary(meteorites)
