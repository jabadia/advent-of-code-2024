from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase
from functools import cmp_to_key

TEST_CASES = [
    TestCase("""
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47    
""", 123)
]


def is_properly_ordered(update, ordering_rules):
    middle_element = update[len(update) // 2]
    for left, right in ordering_rules:
        try:
            left_index = update.index(left)
            right_index = update.index(right)
            if right_index < left_index:
                return 0
        except ValueError:
            assert False, "rule not applicable"
    return middle_element


class Comparator:
    def __init__(self, ordering_rules):
        self.ordering_rules = ordering_rules

    def __call__(self, a, b):
        for left, right in self.ordering_rules:
            if left in (a, b) and right in (a, b):
                return -1 if a == left else 1
        return 0


def solve(input):
    ordering_rules, updates = input.strip().split('\n\n')
    ordering_rules = [tuple(map(int, rule.split('|'))) for rule in ordering_rules.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

    total = 0
    for update in updates:
        applicable_rules = [rule for rule in ordering_rules if rule[0] in update and rule[1] in update]
        if not is_properly_ordered(update, applicable_rules):
            sorted_update = sorted(update, key=cmp_to_key(Comparator(applicable_rules)))
            assert is_properly_ordered(sorted_update, applicable_rules), "bad sorting"
            total += sorted_update[len(sorted_update) // 2]

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
        print("[ERROR] Tests failed")
