from pathlib import Path


def part_1():
    with open(Path(__file__).parent / "input.txt") as file:
        xs = [int(item) for item in file]
        increases = 0
        for x, y in zip(xs, xs[1:]):
            if (x < y):
                increases += 1
        return increases

def part_2():
    with open(Path(__file__).parent / "input.txt") as file:
        xs = [sum(xs[x:x+3]) for x in range(len(xs)-2)]
        increases = 0
        for x, y in zip(xs, xs[1:]):
            if (x < y):
                increases += 1
        return increases


if __name__ == "__main__":
    print(part_1())
    print(part_2())
