# Earth Meteorite Landings Analysis

##  Dataset

This project analyzes Earth meteorite landing data from the following JSON source:

[https://raw.githubusercontent.com/dmachek/meteorites-homework/main/Meteorite-Landings.json](https://raw.githubusercontent.com/dmachek/meteorites-homework/main/Meteorite-Landings.json)

---

##  Goal

* ✅ Extract and process the dataset.
* ✅ Answer the following questions:

  1. How many entries are in the dataset?
  2. What is the name and mass of the most massive meteorite?
  3. What is the most frequent year in the dataset?

⚠️ Please note: the **solution must be submitted as a Pull Request** and must include the code used to obtain the results.

---

## ️ Project Structure

```
.
├── main.py                 # Entry point with CLI interface
├── meteorite.py            # Meteorite class, parser, and logic
├── analyze_pandas.py       # Optional pandas-based implementation
├── utils.py                # Logging and debug helper functions
├── requirements.txt        # Dependencies
└── README.md               # This file
```

---

##  Solution Approach

### Step 1: Understand the Data Format

The dataset contains a deeply nested JSON structure. Before implementing any logic, we reviewed a few entries manually and inspected keys like `Mass`, `Name`, and `Year`.

### Step 2: Build a Robust Parser

In `meteorite.py`, we built a `Meteorite` class that extracts and converts values safely:

* Mass is parsed only if in grams.
* Year is extracted only from valid `DateObject` structures.

All malformed entries are logged and skipped.

### Step 3: CLI Interface

Implemented in `main.py` using `argparse`, with support for:

* Printing all meteorites (`--print-all`)
* Searching by ID or name (`--search-id`, `--search-name`)
* Pandas-based analysis (`--use-pandas`)
* Debug logging (`--debug`)

### Step 4: Optional — Pandas Analysis

If `--use-pandas` is specified, we analyze the same data using `pandas.DataFrame`.

---

##  Usage

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run with default file:

```bash
python main.py
```

### Run with pandas:

```bash
python main.py --use-pandas
```

### Search by name:

```bash
python main.py --search-name=Hope
```

### Print all entries:

```bash
python main.py --print-all
```

---

##  Example Output

```bash
1) Total entries: 45716
2) Heaviest: Hope (60,000,000g)
3) Most frequent year: 2003 (3323 entries)
```

---

##  Tools Used

* Python 3.10
* PyCharm 2025.1.2 (Community Edition)
* pandas
* pytz
* argparse

---
