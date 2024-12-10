from pydoc_data.topics import topics

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase
from utils.timing import timing

TEST_CASES = [
    TestCase("""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""", 36)
]


# 5, 6, 5, 3, 1, 3, 5, 3, 5

def find_score(topomap, pos):
    queue = [pos]
    visited = {pos}
    score = 0
    while queue:
        # print(f'score: {score}, queue: {queue}, visited: {visited}')
        row, col = queue.pop(0)
        height = topomap[row][col]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) in visited:
                continue
            if not (0 <= new_row < len(topomap) and 0 <= new_col < len(topomap[new_row])):
                continue
            new_height = topomap[new_row][new_col]
            if new_height == height + 1:
                visited.add((new_row, new_col))
                if new_height == 9:
                    score += 1
                else:
                    queue.append((new_row, new_col))

    return score


@timing
def solve(input):
    topomap = [[int(height) for height in row] for row in input.strip().split("\n")]

    # for row in topomap:
    #     print(row)

    total_score = 0
    print(len(topomap))
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
