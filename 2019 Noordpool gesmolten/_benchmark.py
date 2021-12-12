'''Usage:
1. Set input files to 'benchmark_input.json'
2. Run this script
'''

import json
import os
import random
import time

DATA_SIZE = 5000

data = {'flats': [], 'sprongen': []}
curr_x = 0
curr_height = random.randint(1, 10)
possible_steps = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                  (1, 0), (1, 1), (1, 2), (1, 3),
                  (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (4, 0)]

for i in range(DATA_SIZE):
    data['flats'].append([curr_x, curr_height])
    next_step = random.choice(possible_steps)
    next_x = curr_x + next_step[0] + 1
    next_height = curr_height + next_step[1]
    if next_height > 10:
        next_height = 10
    if random.choice([0,1,2]):
        next_height = random.randint(1,next_height)
    for x in range(curr_x+1, next_x):
        if random.choice([0,1]):
            data['flats'].append([x, random.randint(1,10)])
    curr_x = next_x
    curr_height = next_height

json_string = json.dumps(data)
with open('benchmark_input.json', 'w') as f:
    f.write(json_string)
    f.close()

t1 = time.time()
import noordpool_gesmolten
t2 = time.time()
time1 = round(t2-t1, 4)

t1 = time.time()
import noordpool_gesmolten_dijkstra
t2 = time.time()
time2 = round(t2-t1, 4)

t1 = time.time()
import noordpool_gesmolten_dijkstra_heapq
t2 = time.time()
time3 = round(t2-t1, 4)

print(f"\n{time1} s - noordpool_gesmolten.py\n\
{time2} s - noordpool_gesmolten_dijkstra.py (slow)\n\
{time3} s - noordpool_gesmolten_dijkstra_heapq.py (fast)")

os.unlink('benchmark_input.json')
