from itertools import product

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""", 11387)
]


def solve(input):
    equations = input.strip().split('\n')
    calibration = 0

    operators = ['*', '+', '||']
    for equation in equations:
        result, terms = equation.split(':')
        terms = list(map(int, terms.split()))
        expected_result = int(result)
        for operator_sequence in product(operators, repeat=len(terms)-1):
            actual_result = terms[0]
            for term, op in zip(terms[1:], operator_sequence):
                if op == '+':
                    actual_result += term
                elif op == '*':
                    actual_result *= term
                elif op == '||':
                    actual_result = int(str(actual_result) + str(term))
            if actual_result == expected_result:
                calibration += expected_result
                break

    return calibration


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
