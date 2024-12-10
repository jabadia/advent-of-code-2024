from pydoc_data.topics import topics

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase
from utils.timing import timing

TEST_CASES = [
    TestCase("""
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
""", 3),
    TestCase("""
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
""", 13),
    TestCase("""
012345
123456
234567
345678
4.6789
56789.
""", 227),
    TestCase("""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""", 81),
]


# 20, 24, 10, 4, 1, 4, 5, 8, 5

def find_score(topomap, pos):
    stack = [(pos, [])]
    score = 0
    while stack:
        (row, col), path = stack.pop()
        height = topomap[row][col]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) in path:
                continue
            if not (0 <= new_row < len(topomap) and 0 <= new_col < len(topomap[new_row])):
                continue
            new_height = topomap[new_row][new_col]
            if new_height == height + 1:
                if new_height == 9:
                    score += 1
                else:
                    stack.append(((new_row, new_col), path + [(row, col)]))

    return score


@timing
def solve(input):
    topomap = [
        [(int(height) if height != '.' else -1) for height in row]
        for row in input.strip().split("\n")
    ]

    # for row in topomap:
    #     print(row)

    total_score = 0
    for row in range(0, len(topomap)):
        for col in range(0, len(topomap[row])):
            if topomap[row][col] == 0:
                print(f"({row:2}, {col:2}) -> ", end='')
                score = find_score(topomap, (row, col))
                print(f"{score:2}")
                total_score += score

    return total_score


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
