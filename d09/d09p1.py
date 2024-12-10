from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
12345
    """, 60),
    TestCase("""
2333133121414131402
""", 1928)
]


def solve(input):
    disk = []
    free = []
    is_file = True
    current_id = 0
    for digit in input.strip():
        digit = int(digit)
        if is_file:
            for _ in range(digit):
                disk.append(current_id)
            current_id += 1
            is_file = False
        else:
            for _ in range(digit):
                disk.append('.')
                free.append(len(disk) - 1)
            is_file = True

    print(''.join([str(digit) for digit in disk]))
    print(free)

    last_sector = len(disk) - 1
    for free_sector in free:
        if last_sector <= free_sector:
            break

        while disk[last_sector] == '.':
            last_sector -= 1
        disk[free_sector] = disk[last_sector]
        disk[last_sector] = '.'
        last_sector -= 1

    print(''.join([str(digit) for digit in disk]))
    return sum(pos * file_id for pos, file_id in enumerate(disk) if file_id != '.')


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
