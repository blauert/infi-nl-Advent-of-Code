# https://aoc.infi.nl/2018/

from collections import defaultdict
import copy

input_file = 'real_input.txt'
#input_file = 'test_input.txt'

with open(input_file, encoding='utf-8') as f:
    doolhof = [list(line.strip()) for line in f.readlines()]

x_max = len(doolhof[0])
y_max = len(doolhof)

"""Generate a grid of coords, field ids, and tegels:
{(0, 0): (0, '╔'), (1, 0): (1, '═'), (2, 0): (2, '╗'), ... }
"""
field_id = 0
grid = {}
for y in range(0, y_max):
    for x in range(0, x_max):
        grid[(x, y)] = (field_id, doolhof[y][x])
        field_id += 1


def generate_graph(grid):
    """Return a graph of field ids and coords:
    {0: {'x': 0, 'y': 0, 'neighbors': {1: {'x': 1, 'y': 0}, 4: {'x': 0, 'y': 1} } }, 1: {...},  ... }
    """
    tegels = {'║': {'up', 'down'}, '╔': {'right', 'down'}, '╗': {'left', 'down'}, '╠': {'up', 'right', 'down'},
              '╦': {'left', 'right', 'down'}, '╚': {'up', 'right'}, '╝': {'up', 'left'},
              '╬': {'up', 'down', 'left', 'right'}, '╩': {'up', 'right', 'left'},
              '═': {'left', 'right'}, '╣': {'up', 'down', 'left'}}

    graph = defaultdict(dict)

    for coords, field in grid.items():
        x = coords[0]
        y = coords[1]

        field_id = field[0]
        tegel = field[1]

        graph[field_id]['x'] = x
        graph[field_id]['y'] = y
        graph[field_id]['neighbors'] = defaultdict(dict)

        if 'right' in tegels[tegel]:
            right_coords = (x+1, y)
            right_neighbor = grid.get(right_coords)
            if right_neighbor is not None and 'left' in tegels[right_neighbor[1]]:
                right_id = right_neighbor[0]
                right = {'x': right_coords[0], 'y': right_coords[1]}
                graph[field_id]['neighbors'][right_id] = right

        if 'left' in tegels[tegel]:
            left_coords = (x-1, y)
            left_neighbor = grid.get(left_coords)
            if left_neighbor is not None and 'right' in tegels[left_neighbor[1]]:
                left_id = left_neighbor[0]
                left = {'x': left_coords[0], 'y': left_coords[1]}
                graph[field_id]['neighbors'][left_id] = left

        if 'down' in tegels[tegel]:
            down_coords = (x, y+1)
            down_neighbor = grid.get(down_coords)
            if down_neighbor is not None and 'up' in tegels[down_neighbor[1]]:
                down_id = down_neighbor[0]
                down = {'x': down_coords[0], 'y': down_coords[1]}
                graph[field_id]['neighbors'][down_id] = down

        if 'up' in tegels[tegel]:
            up_coords = (x, y-1)
            up_neighbor = grid.get(up_coords)
            if up_neighbor is not None and 'down' in tegels[up_neighbor[1]]:
                up_id = up_neighbor[0]
                up = {'x': up_coords[0], 'y': up_coords[1]}
                graph[field_id]['neighbors'][up_id] = up

    return graph


def naar_rechts(grid, rij):
    # Shift row to the right
    new_grid = grid.copy()
    for x in range(x_max):
        new_grid[((x+1) % x_max, rij)] = grid[(x, rij)]
    return new_grid


def naar_beneden(grid, col):
    # Shift column down
    new_grid = grid.copy()
    for y in range(y_max):
        new_grid[(col, (y+1) % y_max)] = grid[(col, y)]
    return new_grid


def stappen_counter(grid):
    # Setup round 1
    start = {'field_id': 0, 'coords': (0, 0), 'visited': set()}
    finish = (x_max-1, y_max-1)
    curr_graph = generate_graph(grid)
    aan_de_beurt = 'rij'
    stappen = 0
    positions = [start]

    # Loop until finished
    while positions:
        temp = []
        print(f"{stappen} steps. Moves to calculate: {len(positions)}")

        # Generate graph for the next round
        if aan_de_beurt == 'rij':
            shifting_rij = stappen % y_max
            grid = naar_rechts(grid, shifting_rij)
        elif aan_de_beurt == 'col':
            shifting_col = stappen % x_max
            grid = naar_beneden(grid, shifting_col)
        next_graph = generate_graph(grid)

        # Modify current graph to reflect Santa being shifted along with shifting rows/cols
        updated_graph = copy.deepcopy(curr_graph)
        for field_id in curr_graph:
            for neighbor_id in curr_graph[field_id]['neighbors']:
                if (
                        (
                            aan_de_beurt == 'rij'
                            and
                            curr_graph[field_id]['neighbors'][neighbor_id]['y'] == shifting_rij
                        )
                    or
                        (
                            aan_de_beurt == 'col'
                            and
                            curr_graph[field_id]['neighbors'][neighbor_id]['x'] == shifting_col
                        )
                ):
                    # Remove shifting neighbors
                    del updated_graph[field_id]['neighbors'][neighbor_id]
                    # Get shifting neighbors' correct coords from next round's graph
                    updated_graph[field_id]['neighbors'][neighbor_id] = {
                        'x': next_graph[neighbor_id]['x'],
                        'y': next_graph[neighbor_id]['y']}

        # Loop through all positions
        for pos in positions:
            curr_id = pos['field_id']
            curr_coords = pos['coords']
            curr_visited = pos['visited'].copy()
            curr_visited.add((curr_id, curr_coords))

            # Check if finished
            if curr_coords == finish:
                print(pos, end='\n\n')
                return stappen

            # Loop through neighbors
            neighbors = updated_graph[curr_id]['neighbors']
            for neighbor_id, n_coords in neighbors.items():
                neighbor_coords = (n_coords['x'], n_coords['y'])
                neighbor = (neighbor_id, neighbor_coords)
                if neighbor not in curr_visited:
                    temp.append({'field_id': neighbor_id, 'coords': neighbor_coords, 'visited': curr_visited})

        # Setup for next round
        curr_graph = next_graph
        if aan_de_beurt == 'rij':
            aan_de_beurt = 'col'
        else:
            aan_de_beurt = 'rij'
        stappen += 1
        positions = temp


print(f"Deel 2: Santa heeft {stappen_counter(grid)} stappen nodig.")
