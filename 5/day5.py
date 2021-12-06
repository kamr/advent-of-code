from pathlib import Path

# def interpolate(x1, x2, y1, y2):
#     points = []
#     if x1 == x2:
#         max_y = max(y1, y2)
#         min_y = min(y1, y2)
#         for y in range(min_y, max_y + 1):
#             points.append((x1, y))
#     if y1 == y2:
#         max_x = max(x1, x2)
#         min_x = min(x1, x2)
#         for x in range(min_x, max_x + 1):
#             points.append((x, y1))
#     if x1 != x2 and y1 != y2:
#         x_step = 1 if x1 < x2 else -1
#         y_step = 1 if y1 < y2 else -1
#         points = [(x1 + i * x_step, y1 + i * y_step) for i in range(abs(x1 - x2) + 1)]
#         print(x1, x2, x_step, y1, y2, y_step, points)
#     return points

def interpolate(x1, x2, y1, y2):
    points = []
    # if x1 == x2:
    #     max_y = max(y1, y2)
    #     min_y = min(y1, y2)
    #     for y in range(min_y, max_y + 1):
    #         points.append((x1, y))
    # if y1 == y2:
    #     max_x = max(x1, x2)
    #     min_x = min(x1, x2)
    #     for x in range(min_x, max_x + 1):
    #         points.append((x, y1))
    # if x1 != x2 and y1 != y2:
    min_y = min(y1, y2)
    min_x = min(x1, x2)
    x_step = 1 if x1 < x2 else -1 if x1 > x2 else 0
    y_step = 1 if y1 < y2 else -1 if y1 > y2 else 0
    length = abs(x1 - x2)
    points = [(x1 + i * x_step, y1 + i * y_step) for i in range(length + 1)]
        # print(x1, x2, x_step, y1, y2, y_step, points)
    return points

def part_1():
    with open(Path(__file__).parent / "input.txt") as file:
        first_occurrence = set()
        second_occurrence = set()
        for line in file:
            xs, ys = line.split(" -> ")
            x1, y1 = [int(a) for a in xs.split(",")]
            x2, y2 = [int(b) for b in ys.split(",")]
            if x1 == x2 or y1 == y2:
                for point in interpolate(x1, x2, y1, y2):
                    if point in first_occurrence:
                        second_occurrence.add(point)
                    else:
                        first_occurrence.add(point)
        return len(second_occurrence)

def part_2():
    with open(Path(__file__).parent / "input.txt") as file:
        first_occurrence = set()
        second_occurrence = set()
        for line in file:
            xs, ys = line.split(" -> ")
            x1, y1 = [int(a) for a in xs.split(",")]
            x2, y2 = [int(b) for b in ys.split(",")]
            for point in interpolate(x1, x2, y1, y2):
                if point in first_occurrence:
                    second_occurrence.add(point)
                else:
                    first_occurrence.add(point)
        return len(second_occurrence)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
