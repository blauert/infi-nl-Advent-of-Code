# https://aoc.infi.nl/2017/

input_file = 'input.txt'

with open(input_file) as file:
    raw_data = file.read()

data = raw_data.split('](')

robots = [robot.strip('[') for robot in data[0].split('][')]
moves = [move.strip(')') for move in data[1].split(')(')]

robots = [[int(i) for i in bot.split(',')] for bot in robots]
moves = [[int(i) for i in move.split(',')] for move in moves]

botsingen = 0
knelpunten = []
for i in range(0, len(moves), len(robots)):
    for j in range(len(robots)):
        current_robot = j
        current_move = i + j
        robots[current_robot][0] += moves[current_move][0]  # x
        robots[current_robot][1] += moves[current_move][1]  # y
    botsing = True
    robot1 = robots[0]
    for robot in robots[1:]:
        if robot != robot1:
            botsing = False
    if botsing:
        knelpunten.append([robots[current_robot][0], robots[current_robot][1]])
        botsingen += 1

print(f"Deel 1: {botsingen}")


# Deel 2

x_max = max([punt[0] for punt in knelpunten])
y_max = max([punt[1] for punt in knelpunten])
knelmap = [[' ' for i in range(x_max+1)] for i in range(y_max+1)]
for punt in knelpunten:
    knelmap[punt[1]][punt[0]] = '#'

print("Deel 2:")
for row in knelmap:
    for char in row:
        print(char, end='')
    print()
