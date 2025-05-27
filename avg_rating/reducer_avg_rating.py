#!/usr/bin/env python3
import sys

current_brand = None
total = 0
count = 0

for line in sys.stdin:
    brand, rating = line.strip().split('\t')
    rating = float(rating)

    if brand == current_brand:
        total += rating
        count += 1
    else:
        if current_brand:
            print(f"{current_brand}\t{total / count:.2f}")
        current_brand = brand
        total = rating
        count = 1

if current_brand:
    print(f"{current_brand}\t{total / count:.2f}")
