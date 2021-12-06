from pathlib import Path
from functools import reduce

def part_1_for():
    with open(Path(__file__).parent / "input.txt") as file:
        xss = file.read().splitlines()
        gamma = epsilon = 0
        rows = len(xss)
        counter = [0] * len(xss[0])
        for xs in xss:
            for i, x in enumerate(xs):
                counter[i] += int(x)
        for i, x in enumerate(counter):
            increment = pow(2, len(counter) - i - 1)
            if x * 2 > rows:
                gamma += increment
            else:
                epsilon += increment
        return gamma * epsilon

def part_1_list_comp():
    with open(Path(__file__).parent / "input.txt") as file:
        xss = file.read().splitlines()
        print(xss)
        ys = [sum([int(row[i]) for row in xss]) for i in range(len(xss[0]))]
        ys = [pow(2, i) if 2*x > len(xss) else 0 for i, x in enumerate(reversed(ys))]
        gamma = sum(ys)
        epsilon = pow(2, len(xss[0])) - gamma - 1
        return gamma * epsilon

def part_1_zip():
    with open(Path(__file__).parent / "input.txt") as file:
        result = file.read().splitlines()
        HALF_LENGTH = len(result) / 2

        gamma = ['1' if x.count('1') > HALF_LENGTH else '0' for x in zip(*result)]
        epsilon = ['0' if x.count('1') > HALF_LENGTH else '1' for x in zip(*result)]

        gamma = int(''.join(gamma), base=2)
        epsilon = int(''.join(epsilon), base=2)

        return gamma * epsilon

def part_2():
    with open(Path(__file__).parent / "input.txt") as file:
        result = file.read().splitlines()
        xs = ys = result

        i = 0
        while len(xs) > 1 or len(ys) > 1:
            if len(xs) > 1:
                mcd = '1' if list(zip(*xs))[i].count('1') >= len(xs) / 2 else '0'
                xs = [x for x in xs if x[i] == mcd]
            if len(ys) > 1:
                lcd = '1' if list(zip(*ys))[i].count('1') < len(ys) / 2 else '0'
                ys = [y for y in ys if y[i] == lcd]
            i += 1

        oxygen = int(xs[0], base=2)
        carbon = int(ys[0], base=2)

        return oxygen * carbon


if __name__ == "__main__":
    print(part_1_for())
    print(part_1_list_comp())
    print(part_1_zip())
    print(part_2())
