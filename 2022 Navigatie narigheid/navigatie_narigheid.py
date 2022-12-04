# https://aoc.infi.nl/2022/

input_file = 'real_input.txt'
#input_file = 'test_input.txt'

with open(input_file) as file:
    instructies = [line.split() for line in file.readlines()]


def draai(richting, graden):
    return (richting + graden) % 360


def stap(positie, richting, stappen):
    x, y = positie
    if richting == 0:
        y += stappen
    elif richting == 45:
        x += stappen
        y += stappen
    elif richting == 90:
        x += stappen
    elif richting == 135:
        x += stappen
        y -= stappen
    elif richting == 180:
        y -= stappen
    elif richting == 225:
        x -= stappen
        y -= stappen
    elif richting == 270:
        x -= stappen
    elif richting == 315:
        x -= stappen
        y += stappen
    return x, y


positie = (0, 0)
richting = 0
spoor = set()

for instr, val in instructies:
    val = int(val)
    if instr == 'draai':
        richting = draai(richting, val)
    elif instr == 'loop':
        stappen = 1
        if val < 0:
            stappen = -1
        for _ in range(abs(val)):
            positie = stap(positie, richting, stappen)
            spoor.add(positie)
    elif instr == 'spring':
        positie = stap(positie, richting, val)
        spoor.add(positie)

print(f"Manhattan afstand: {abs(positie[0]) + abs(positie[1])}")

rows = []
for y in range(6, -1, -1):
    col = ''
    for x in range(91):
        if (x, y) in spoor:
            col += '#'
        else:
            col += '.'
    rows.append(col)

for row in rows:
    print(row)