from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""", 6)
]

# turning right picking up the next direction
directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def is_loop(rows, guard):
    direction = 0  # up
    visited_positions = {(direction, guard)}

    while True:
        # try move forward
        next_guard = (guard[0] + directions[direction][0], guard[1] + directions[direction][1])
        if next_guard[0] < 0 or next_guard[0] >= len(rows) or next_guard[1] < 0 or next_guard[1] >= len(rows[0]):
            # guard left
            return False
        elif (direction, next_guard) in visited_positions:
            return True

        if rows[next_guard[0]][next_guard[1]] == '#':
            direction = (direction + 1) % 4  # turn right
        else:
            guard = next_guard  # move forward
            visited_positions.add((direction, guard))

    assert False, "unreachable"


def solve(input):
    rows = [list(row) for row in input.strip().split('\n')]
    guard = None
    for row in range(len(rows)):
        if '^' in rows[row]:
            guard = (row, rows[row].index('^'))
            break

    loops = 0
    for row in range(len(rows)):
        for col in range(len(rows[row])):
            next_rows = [row.copy() for row in rows]
            next_rows[row][col] = '#'
            if is_loop(next_rows, guard):
                loops += 1

    return loops


if __name__ == '__main__':
    input = fetch_input()
    success = True
    for case in TEST_CASES:
        result = solve(case.case)
        success = success and case.check(result)

    if success:
        answer = solve(input)
        print(answer)
        submit_answer(answer)
    else:
        print("[ERROR] Tests failed")
