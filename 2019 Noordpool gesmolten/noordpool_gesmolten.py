# https://aoc.infi.nl/2019/

import json

input_file = 'real_input.json'
#input_file = 'test_input.json'
#input_file = 'benchmark_input.json'

with open(input_file) as f:
    data = json.load(f)

huizen = {x: y for x, y in data['flats']}


# Deel 1

sprongen = data['sprongen']
positie = data['flats'][0].copy()
stappen = 0

for sprong in sprongen:
    positie[0] += sprong[0] + 1  # x
    positie[1] += sprong[1]  # y
    stappen += 1
    y = huizen.get(positie[0])
    if y is not None and y <= positie[1]:
        # Reached last house
        if positie[0] == data['flats'][-1][0]:
            stappen = 0
            break
        positie[1] = y
    else:  # No house in position x or house too high
        break

print(f"Deel 1: Na {stappen} stappen valt de kerstman op de grond.")


# Deel 2

start = tuple(data['flats'][0])  # (x, y)
finish = data['flats'][-1][0]  # x

# {x1: None, x2: None, etc...}
cost_per_house = {huis[0]: float('inf') for huis in data['flats'][1:]}

# {(x, y): cost}
possible_steps = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4,
                  (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 4,
                  (2, 0): 2, (2, 1): 3, (2, 2): 4,
                  (3, 0): 3, (3, 1): 4,
                  (4, 0): 4}

combinations = [{'position': start, 'energy_used': 0, 'steps': [], 'route': set()}]


while combinations:
    temp = []
    positions_updated = set()

    for comb in combinations:

        # Discard combinations that already went through recently updated points
        # - thus necessarily at a higher cost - in a PREVIOUS round
        if not positions_updated & comb['route']:

            # Simulate next jumps
            for step, cost in possible_steps.items():

                # Update position
                x = comb['position'][0] + step[0] + 1
                y = comb['position'][1] + step[1]
                rooftop = huizen.get(x)
                if rooftop is not None and y >= rooftop:
                    position = (x, rooftop)
                else:
                    position = None

                # Update energy usage
                energy_used = comb['energy_used'] + cost

                # Update cost to reach current position
                if position and energy_used < cost_per_house[x]:
                    cost_per_house[x] = energy_used
                    positions_updated.add(x)

                    # Update steps
                    steps = comb['steps'].copy()
                    steps.append([step[0], step[1]])
                    # Update route
                    route = comb['route'] | set([x])
                    # Update combination
                    new_comb = {'position': position,
                                'energy_used': energy_used,
                                'steps': steps,
                                'route': route}

                    # Discard combinations that already went through current point
                    # - thus necessarily at a higher cost - in the CURRENT round
                    temp = [c for c in temp if not x in c['route']]

                    # Send combination to the next round, or get result
                    if x != finish:
                        temp.append(new_comb)
                    else:
                        result_steps = new_comb['steps']

    combinations = temp

print(f"Deel 2: Het meest efficiente pad kost {cost_per_house[finish]} energie.")
print(f"\nSprongen voor simulatie op de site:\n{result_steps}")
