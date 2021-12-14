# https://aoc.infi.nl/2017/

input_file = 'input.txt'

with open(input_file) as file:
    raw_data = file.read()

data = raw_data.split('](')

robots = [robot.strip('[') for robot in data[0].split('][')]
moves = [move.strip(')') for move in data[1].split(')(')]

robots = [[int(i) for i in bot.split(',')] for bot in robots]
moves = [[int(i) for i in move.split(',')] for move in moves]

knelpunten = 0
knelmoves = []
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
        knelmoves.append(i)
        knelpunten += 1

print(f"Deel 1: {knelpunten}")

# Deel 2

pattern = []
for i in range(len(knelmoves)-1):
    pattern.append(knelmoves[i+1] - knelmoves[i])

print(set(pattern))
