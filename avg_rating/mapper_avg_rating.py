#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    try:
        brand = row[1].strip().lower().replace(" ", "")
        rating = float(row[3])
        if brand:
            print(f"{brand}\t{rating}")
    except:
        continue
