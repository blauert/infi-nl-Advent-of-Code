# https://aoc.infi.nl/2020/


def aantal_pakjes_in_zak(side_length):
    pakjes_curr = side_length
    pakjes = 0
    for i in range(side_length):
        pakjes += pakjes_curr
        pakjes_curr += 2
    middle = side_length * pakjes_curr
    pakjes *= 2
    pakjes += middle
    return pakjes


def kleinste_zak(goal, step=1):
    guess = {'low': 0, 'high': float('inf')}
    # Guess
    while guess['high'] == float('inf'):
        curr = guess['low'] + step
        aantal_pakjes = aantal_pakjes_in_zak(curr)
        if aantal_pakjes < goal:
            guess['low'] = curr
        elif aantal_pakjes >= goal:
            guess['high'] = curr
    # Bisect
    while guess['high'] > (guess['low'] + 1):
        half = guess['high'] - (guess['high'] - guess['low']) // 2
        aantal_pakjes = aantal_pakjes_in_zak(half)
        if aantal_pakjes < goal:
            guess['low'] = half
        elif aantal_pakjes >= goal:
            guess['high'] = half
    return guess['high']


# Deel 1

pakjes_goal = 17488031
side_len = kleinste_zak(pakjes_goal)
print(f"Side length required for {pakjes_goal} pakjes: {side_len}")


# Deel 2

pakjes_goals = [4541682716, 1340798729, 747740862, 430796666, 368939948, 42728646]
stukken_stof = 0

for pakjes_goal in pakjes_goals:
    stukken_stof += kleinste_zak(pakjes_goal, step=3000) * 8

print(f"Stukken stof required for alle zakken: {stukken_stof}")