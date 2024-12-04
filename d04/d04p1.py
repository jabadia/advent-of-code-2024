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
""", 18)
]

def get_letters(lines, pos, direction, count):
    letters = lines[pos[0]][pos[1]]
    for i in range(1, count):
        pos = pos[0] + direction[0], pos[1] + direction[1]
        if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
            return letters
        letters += lines[pos[0]][pos[1]]
    return letters


def solve(input):
    lines = input.strip().split('\n')
    word = 'XMAS'

    count = 0

    # find horizontal
    count += sum([line.count(word) for line in lines])
    count += sum([line[::-1].count(word) for line in lines])

    # find vertical
    for i in range(len(lines[0])):
        column = ''.join([line[i] for line in lines])
        count += column.count(word)
        count += column[::-1].count(word)

    # find diagonal
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'X':
                letters = get_letters(lines, (row, col), (1, 1), len(word))
                count += 1 if letters == word else 0
                letters = get_letters(lines, (row, col), (1, -1), len(word))
                count += 1 if letters == word else 0
                letters = get_letters(lines, (row, col), (-1, 1), len(word))
                count += 1 if letters == word else 0
                letters = get_letters(lines, (row, col), (-1, -1), len(word))
                count += 1 if letters == word else 0

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
