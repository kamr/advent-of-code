from pathlib import Path

WIDTH = 5
SQUARES = WIDTH * WIDTH

def check_win(marks, row, column):
    row_marks = marks[row]
    column_marks = [marks[i][column] for i in range(WIDTH)]
    return all(row_marks) or all(column_marks)

def board_score(board, marks, draw):
    board = sum(board, [])
    zipped = list(zip(board, marks))
    unmarked = [value for bool, value in zipped if not bool]
    return sum(unmarked) * draw

def part_1():
    with open(Path(__file__).parent / "input.txt") as file:
        result = file.read().splitlines()
        draw = list(map(int, result[0].split(",")))
        boards = [x.strip().replace("  ", " ").split(" ") for x in result[1:] if x != '']
        boards = list(map(int, sum(boards, [])))
        NUM_BOARDS = int(len(boards) / (SQUARES))
        marks = [[[False for i in range(WIDTH)] for j in range(WIDTH)]for k in range(NUM_BOARDS)]
        for d in draw:
            matching_positions = [i for i, x in enumerate(boards) if d == x]
            for m in matching_positions:
                board = int(m / SQUARES)
                row = int(m % SQUARES / 5)
                column = m % 5
                marks[board][row][column] = True
                if check_win(marks[board], row, column):
                    return board_score(marks[board], boards[board * SQUARES:(board + 1) * SQUARES], d)
        return "No winner"

def part_2():
    with open(Path(__file__).parent / "input.txt") as file:
        result = file.read().splitlines()
        draw = list(map(int, result[0].split(",")))
        boards = [x.strip().replace("  ", " ").split(" ") for x in result[1:] if x != '']
        boards = list(map(int, sum(boards, [])))
        NUM_BOARDS = int(len(boards) / (SQUARES))
        marks = [[[False for i in range(WIDTH)] for j in range(WIDTH)]for k in range(NUM_BOARDS)]
        winners = [False] * NUM_BOARDS
        for d in draw:
            matching_positions = [i for i, x in enumerate(boards) if d == x]
            for m in matching_positions:
                board = int(m / SQUARES)
                row = int(m % SQUARES / 5)
                column = m % 5
                marks[board][row][column] = True
                if check_win(marks[board], row, column):
                    winners[board] = True
                if sum(winners) == NUM_BOARDS:
                    return board_score(marks[board], boards[board * SQUARES:(board + 1) * SQUARES], d)
        return "No winner"

if __name__ == "__main__":
    print(part_1())
    print(part_2())
