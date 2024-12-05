from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

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
""", 143)
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
            continue  # rule not applicable
    return middle_element


def solve(input):
    ordering_rules, updates = input.strip().split('\n\n')
    ordering_rules = [list(map(int, rule.split('|'))) for rule in ordering_rules.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

    return sum(is_properly_ordered(update, ordering_rules) for update in updates)


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
