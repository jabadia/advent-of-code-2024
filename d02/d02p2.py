from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""", 4)
]


def is_safe_inner(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False

    for level0, level1 in zip(report, report[1:]):
        if not (1 <= abs(level0 - level1) <= 3):
            return False

    return True


def is_safe(report):
    report = [int(n) for n in report.split()]

    if is_safe_inner(report):
        return True

    for i in range(len(report)):
        dampened = report[:i] + report[i+1:]
        if is_safe_inner(dampened):
            return True

    return False

def solve(input):
    return sum(is_safe(report) for report in input.strip().split("\n"))


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
