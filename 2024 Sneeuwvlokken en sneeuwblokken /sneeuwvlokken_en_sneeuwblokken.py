# https://aoc.infi.nl/2024

input_file = 'real_input.txt'
#input_file = 'test_input.txt'

with open(input_file) as file:
    instructies = [line.split() for line in file.readlines()]


class StackMachine():

    def __init__(self, x, y, z):
        self.program_counter = 0
        self.stack = []
        self.coords = {'x': x, 'y': y, 'z': z}
        self.done = False

    def __push(self, value):
        self.stack.append(value)

    def __add(self):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def __jmpos(self, offset):
        if self.stack.pop() >= 0:
            self.program_counter += offset

    def __ret(self):
        self.done = True

    def run(self, num, instr):
        if num == self.program_counter:
            if len(instr) == 2:
                if instr[1].lstrip('-').isdigit():
                    arg = int(instr[1])
                else:
                    arg = self.coords[instr[1].lower()]
            match instr[0]:
                case 'push':
                    self.__push(arg)
                case 'add':
                    self.__add()
                case 'jmpos':
                    self.__jmpos(arg)
                case 'ret':
                    self.__ret()
            self.program_counter += 1


def sky_scanner(x_max, y_max, z_max):
    blokjes_som = 0
    wolken = {}
    for x in range(x_max):
        print(f"Pass {x+1}/{x_max}...")
        for y in range(y_max):
            for z in range(z_max):
                xm_4s = StackMachine(x, y, z)
                for num, ins in enumerate(instructies):
                    xm_4s.run(num, ins)
                    if xm_4s.done:
                        sneeuwdata = xm_4s.stack[-1]
                        blokjes_som += sneeuwdata
                        wolken[(x, y, z)] = sneeuwdata > 0
                        break
    return blokjes_som, wolken


def get_neighbors(coords):
    x, y, z = coords
    return set([(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)])


def is_cloud(wolken, coords):
    res = wolken.get(coords)
    if res is not None:
        if res:
            return True
    return False


def count_clouds(wolken, x_max, y_max, z_max):
    count = 0
    visited = set()
    for x in range(x_max):
        for y in range(y_max):
            for z in range(z_max):
                cur = (x, y, z)
                cur_is_cloud = False
                to_do = set([cur])
                while to_do:
                    cur = to_do.pop()
                    if cur not in visited:
                        visited.add(cur)
                        if is_cloud(wolken, cur):
                            if not cur_is_cloud:
                                cur_is_cloud = True
                            to_do |= get_neighbors(cur)
                if cur_is_cloud:
                    count += 1
    return count


blokjes_som, wolken = sky_scanner(30, 30, 30)

# Deel 1

print(f"Som van alle blokjes: {blokjes_som}")

# Deel 2

print(f"Wolken: {count_clouds(wolken, 30, 30, 30)}")