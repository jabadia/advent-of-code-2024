from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
3   4
4   3
2   5
1   3
3   9
3   3
""", 11)
]


def solve(input):
    lines = input.strip(' \n').split('\n')
    lefts, rights = [], []
    for line in lines:
        left, right = [int(n) for n in filter(None, line.split(' '))]
        lefts.append(left)
        rights.append(right)

    lefts = sorted(lefts)
    rights = sorted(rights)

    distances = 0
    for (left, right) in zip(lefts, rights):
        distances += abs(left - right)

    return distances


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
