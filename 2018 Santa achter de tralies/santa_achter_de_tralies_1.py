# https://aoc.infi.nl/2018/

from collections import defaultdict

input_file = 'real_input.txt'
#input_file = 'test_input.txt'

with open(input_file, encoding='utf-8') as f:
    doolhof = [list(line.strip()) for line in f.readlines()]

x_max = len(doolhof[0])
y_max = len(doolhof)

start = (0, 0)
finish = (x_max-1, y_max-1)

grid = {}
for y in range(0, y_max):
    for x in range(0, x_max):
        grid[(x, y)] = doolhof[y][x]


def generate_graph(grid):

    graph = defaultdict(list)

    tegels = {'║': {'up', 'down'}, '╔': {'right', 'down'}, '╗': {'left', 'down'}, '╠': {'up', 'right', 'down'},
              '╦': {'left', 'right', 'down'}, '╚': {'up', 'right'}, '╝': {'up', 'left'},
              '╬': {'up', 'down', 'left', 'right'}, '╩': {'up', 'right', 'left'},
              '═': {'left', 'right'}, '╣': {'up', 'down', 'left'}}

    for point, tegel in grid.items():
        x = point[0]
        y = point[1]

        if 'right' in tegels[tegel]:
            right = (x+1, y)
            right_neighbor = grid.get(right)
            if right_neighbor is not None and 'left' in tegels[right_neighbor]:
                graph[point].append(right)

        if 'left' in tegels[tegel]:
            left = (x-1, y)
            left_neighbor = grid.get(left)
            if left_neighbor is not None and 'right' in tegels[left_neighbor]:
                graph[point].append(left)

        if 'down' in tegels[tegel]:
            down = (x, y+1)
            down_neighbor = grid.get(down)
            if down_neighbor is not None and 'up' in tegels[down_neighbor]:
                graph[point].append(down)

        if 'up' in tegels[tegel]:
            up = (x, y-1)
            up_neighbor = grid.get(up)
            if up_neighbor is not None and 'down' in tegels[up_neighbor]:
                graph[point].append(up)

    return graph


def stappen_counter():
    graph = generate_graph(grid)
    stappen = -1  # start with 0 steps on start (0, 0)
    positions = set([start])
    visited = set()
    while positions:
        temp = set()
        stappen += 1
        for pos in positions:
            visited.add(pos)
            if pos == finish:
                return stappen
            neighbors = graph[pos]
            for neighbor in neighbors:
                if neighbor not in visited:
                    temp.add(neighbor)
        positions = temp


print(f"Deel 1: Santa heeft {stappen_counter()} stappen nodig.")
