# https://aoc.infi.nl/2021

from collections import defaultdict
from copy import deepcopy

mode = 'real'
#mode = 'test'

if mode == 'real':
    print("Using real data")
    input_file = 'speelgoedlijst.txt'
    ingepakt = 20
elif mode == 'test':
    print("Using test data")
    input_file = 'speelgoedlijst_test.txt'
    ingepakt = 3

with open(input_file) as file:
    lijst = file.readlines()

missende_onderdelen = int(lijst[0].split()[0])

speelgoedlijst = defaultdict(dict)
for line in lijst[1:]:
    line_split = line.split()
    item = line_split[0].replace(':', '')
    parts = line_split[1:]
    for i in range(0, len(parts), 2):
        count = int(parts[i])
        part = parts[i+1].replace(',', '')
        speelgoedlijst[item][part] = count


# Deel 1

def deel1(speelgoedlijst):

    speelgoedlijst = deepcopy(speelgoedlijst)
    parts_count = {}

    # Find the basic building blocks
    for item, parts in speelgoedlijst.items():
        parts_done = []
        for part in parts:
            if part not in speelgoedlijst:
                parts_done.append(part)
        for part in parts_done:
            count = parts.pop(part)
            parts_count.setdefault(item, 0)
            parts_count[item] += count

    # Multiply remaining parts with their respective subparts
    done = False
    while not done:
        done = True
        for item, parts in speelgoedlijst.items():
            parts_done = []
            for part in parts:
                if part in parts_count and not speelgoedlijst[part]:
                    parts_done.append(part)
                else:
                    done = False
            for part in parts_done:
                count = parts.pop(part) * parts_count[part]
                parts_count.setdefault(item, 0)
                parts_count[item] += count

    print(f"Deel 1: {max(parts_count.values())}")
    return parts_count


parts_count = deel1(speelgoedlijst)


# Deel 2

def deel2():

    onderdelen = set()
    for items in speelgoedlijst.values():
        for item in items.keys():
            onderdelen.add(item)

    speelgoed = []
    for item in speelgoedlijst.keys():
        if item not in onderdelen:
            speelgoed.append(item)

    combinations = {}
    for item in speelgoed:
        parts = parts_count[item]
        combinations[parts] = [item]

    for i in range(ingepakt-1):
        combinations_updated = {}
        for count, comb in combinations.items():
            for item in speelgoed:
                item_count = parts_count[item]
                new_count = count + item_count
                # Discard combinations whose count is too large
                if new_count <= missende_onderdelen:
                    # Skip other combinations of same count
                    if new_count not in combinations_updated:
                        new_comb = comb + [item]
                        # Get result in last generation of combinations
                        if new_count == missende_onderdelen and i == ingepakt - 2:
                            result = sorted([word[0] for word in new_comb])
                            result_string = ''
                            for letter in result:
                                result_string += letter
                            print(f"Deel 2: {result_string}")
                            return
                        combinations_updated[new_count] = new_comb
        combinations = combinations_updated


deel2()
