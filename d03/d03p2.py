import re

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""", 48)
]


def solve(input):
    total = 0
    enabled = True
    for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", input.strip()):
        if match.group(0) == 'do()':
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        elif enabled:
            total += int(match.group(1)) * int(match.group(2))

    return total


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
        print("Tests failed")
