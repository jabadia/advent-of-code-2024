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
""", 41)
]

# turning right picking up the next direction
directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def solve(input):
    rows = [list(row) for row in input.strip().split('\n')]
    direction = 0  # up
    guard = None
    for row in range(len(rows)):
        if '^' in rows[row]:
            guard = (row, rows[row].index('^'))
            break

    rows[guard[0]][guard[1]] = 'X'
    while True:
        # move forward
        next_guard = (guard[0] + directions[direction][0], guard[1] + directions[direction][1])
        if next_guard[0] < 0 or next_guard[0] >= len(rows) or next_guard[1] < 0 or next_guard[1] >= len(rows[0]):
            # guard left
            break
        if rows[next_guard[0]][next_guard[1]] == '#':
            direction = (direction + 1) % 4  # turn right
        else:
            guard = next_guard  # move forward
            rows[guard[0]][guard[1]] = 'X'

    return sum([row.count('X') for row in rows])


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
