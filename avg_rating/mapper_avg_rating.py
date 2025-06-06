#!/usr/bin/env python3
import sys
import csv
import re

# Brand cleaning function
brand_aliases = {
    "samsybg": "samsung",
    "samssung": "samsung",
    "samsung": "samsung",
    "samsunggalaxyinternationalinc": "samsung",
    "samsungstraighttalk": "samsung",
    "samsybggalaxy": "samsung",
    "samsungkorea": "samsung",
    "samsungkorealtd": "samsung",
    "samsunginternational": "samsung",
    "samsunggalaxy": "samsung",
    "samsung/straighttalk": "samsung",
    "lgelectronicsmobilecommusa": "lg",
    "lgelectronics": "lg",
    "lgelectronic": "lg",
    "htcamerica": "htc",
    "applecomputer": "apple",
    "rim": "blackberry",
    "blackberryrim": "blackberry",
    "blackberrry": "blackberry",
    "blackberrystorm9530smartphoneunlockedgsmwirelesshandhelddevicewcamerabluetooth325touchscreenlcd": "blackberry",
    "motorolax2ndgenxt1093": "motorola",
    "googlepixel": "google",
    "thenokia": "nokia",
    "sonimtechnologies": "sonim",
    "sonyericssonmobile": "sonyericsson",
    "sonyEricssonmobile": "sonyericsson",
    "sony/ericsson": "sonyericsson",
    "indigi®": "indigi",
}


def clean_brand(raw_brand):
    # checks if the input raw_brand is empty
    if not raw_brand:
        return ""
    brand = raw_brand.lower().strip().replace(" ", "")
    brand = re.sub(r"[^a-z0-9]", "", brand)  # Removing all non-alphanumeric chars
    return brand_aliases.get(brand, brand)  # Return mapped alias if exists


reader = csv.reader(sys.stdin)
for row in reader:
    try:
        brand = clean_brand(row[1])
        rating = float(row[3])
        if brand:
            print(f"{brand}\t{rating}")
    except:
        continue
