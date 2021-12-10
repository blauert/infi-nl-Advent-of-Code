# https://aoc.infi.nl/2020/

def side_count(goal, start=1, step=1):
    side_length = start
    if step == 0:
        print("Error! Step size should not be 0.")
        return 0
    while True:
        pakjes = 0
        pakjes_curr = side_length
        for i in range(side_length):
            pakjes += pakjes_curr
            pakjes_curr += 2
        middle = side_length * pakjes_curr
        pakjes *= 2
        pakjes += middle
        if step > 0 and pakjes >= goal:
            return side_length
        if step == -1 and pakjes <= goal:
            return side_length - step
        elif step < 0 and pakjes <= goal:
            return side_length + step
        side_length += step


# Deel 1

pakjes_goal = 17485880
side_len = side_count(pakjes_goal)

print(f"Side length required for {pakjes_goal} pakjes: {side_len}")


# Deel 2

# Steps should alternate between consecutively decreasing positive and negative values,
STEPS = [1000, -100, 10, -1]  # with the last step size being either 1, or -1.

pakjes_goals = [4541682716, 1340798729, 747740862, 430796666, 368939948, 42728646]
stukken_stof = 0
for pakjes_goal in pakjes_goals:
    best_guess = 1000
    for step in STEPS:
        best_guess = side_count(pakjes_goal, best_guess, step)
    stukken_stof += best_guess * 8

print(f"Stukken stof required for alle zakken: {stukken_stof}")
