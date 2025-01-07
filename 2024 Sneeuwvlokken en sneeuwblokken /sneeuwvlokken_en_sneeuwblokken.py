# https://aoc.infi.nl/2024

#input_file = 'real_input.txt'
input_file = 'test_input.txt'

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


def blokjes_som(x_max, y_max, z_max):
    b_sum = 0
    for x in range(x_max):
        print(f"Pass {x+1}/{x_max}...")
        for y in range(y_max):
            for z in range(z_max):
                xm_4s = StackMachine(x, y, z)
                for num, ins in enumerate(instructies):
                    xm_4s.run(num, ins)
                    if xm_4s.done:
                        b_sum += xm_4s.stack[-1]
                        break
    return b_sum


# Deel 1

print(f"Som van alle blokjes: {blokjes_som(30,30,30)}")


# Deel 2
