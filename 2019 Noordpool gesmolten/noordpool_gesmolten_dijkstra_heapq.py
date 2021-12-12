# https://aoc.infi.nl/2019/

import heapq
import json

input_file = 'real_input.json'
#input_file = 'test_input.json'
#input_file = 'benchmark_input.json'

with open(input_file) as f:
    data = json.load(f)

huizen = {x: y for x, y in data['flats']}


# Deel 2 using textbook Dijkstra'a algorithm with heapq (fast)

possible_steps = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4,
                  (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 4,
                  (2, 0): 2, (2, 1): 3, (2, 2): 4,
                  (3, 0): 3, (3, 1): 4,
                  (4, 0): 4}

# Building the graph

graph = {}

for house, height in huizen.items():
    start_children = {}
    for step, cost in possible_steps.items():
        x = house + step[0] + 1
        y = height + step[1]
        rooftop = huizen.get(x)
        if rooftop is not None and y >= rooftop:
            if start_children.get(x, float('inf')) > cost:
                start_children[x] = cost
    graph[house] = start_children


# Dijkstra's algorithm

start = data['flats'][0][0]
finish = data['flats'][-1][0]

costs = {house[0]: float('inf') for house in data['flats'][1:]}
costs[start] = 0

parents = {}
processed = set()

min_dist = [(0, start)]

while min_dist:

    cur_dist, cur = heapq.heappop(min_dist)
    if cur in processed:
        continue
    processed.add(cur)

    for neighbor in graph[cur]:
        if neighbor in processed:
            continue
        this_dist = cur_dist + graph[cur][neighbor]
        if this_dist < costs[neighbor]:
            costs[neighbor] = this_dist
            heapq.heappush(min_dist, (this_dist, neighbor))

print(f"Deel 2: Het meest efficiente pad kost {costs[finish]} energie.")
