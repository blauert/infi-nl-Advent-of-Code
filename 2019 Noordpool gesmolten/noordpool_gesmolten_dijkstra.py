# https://aoc.infi.nl/2019/

import json

input_file = 'real_input.json'
#input_file = 'test_input.json'

with open(input_file) as f:
    data = json.load(f)

huizen = {x: y for x, y in data['flats']}


# Deel 2 using textbook Dijkstra'a algorithm
# (runs slower than other solution)

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


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = start
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)

print(f"Deel 2: Het meest efficiente pad kost {costs[finish]} energie.")
