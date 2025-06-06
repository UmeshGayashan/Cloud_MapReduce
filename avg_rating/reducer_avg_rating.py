#!/usr/bin/env python3
import sys

current_brand = None
total = 0
count = 0

# each line of input from mapper
for line in sys.stdin:
    # removes any leading or trailing whitespace and splits the line into two parts at the tab (\t)
    brand, rating = line.strip().split('\t')
    # from a string to a float
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
# last brand in the input
if current_brand:
    print(f"{current_brand}\t{total / count:.2f}")
