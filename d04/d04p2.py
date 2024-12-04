from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""", 9)
]


def get_safe_letter(lines, pos):
    if 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0]):
        return lines[pos[0]][pos[1]]
    return 'Z'


def get_cross_arms(lines, pos):
    return sorted([
        get_safe_letter(lines, (pos[0] - 1, pos[1] - 1)),
        get_safe_letter(lines, (pos[0] + 1, pos[1] + 1)),
    ]), sorted([
        get_safe_letter(lines, (pos[0] + 1, pos[1] - 1)),
        get_safe_letter(lines, (pos[0] - 1, pos[1] + 1)),
    ])


def solve(input):
    lines = input.strip().split('\n')

    count = 0

    # find X-MAS
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'A':
                arms = get_cross_arms(lines, (row, col))
                if arms[0] == ['M', 'S'] and arms[1] == ['M', 'S']:
                    count += 1

    return count


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
