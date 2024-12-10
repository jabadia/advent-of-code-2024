from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase
from utils.timing import timing

TEST_CASES = [
    # TestCase("""12345""", 23),
    TestCase("""
2333133121414131402
""", 2858)
]


def print_disk(files):
    disk_size = max(start_pos + file_length for start_pos, file_length in files)
    disk = ['.' for _ in range(disk_size)]
    for file_id, (start_pos, file_length) in enumerate(files):
        for i in range(start_pos, start_pos + file_length):
            disk[i] = str(file_id)
    print(''.join(disk))


@timing
def solve(input):
    files = []  # index is file_id, tuple of (start_pos, file_length)
    free = []  # list of free spaces (start_pos, length)
    is_file = True
    current_id = 0
    start_pos = 0
    for digit in input.strip():
        digit = int(digit)
        if is_file:
            files.append((start_pos, digit))
            start_pos += digit
            current_id += 1
            is_file = False
        else:
            free.append((start_pos, digit))
            start_pos += digit
            is_file = True

    if len(files) <= 10:
        print(files)
        print_disk(files)
        print(free)
        print('-')

    for file_id, (start_pos, file_length) in enumerate(reversed(files)):
        file_id = len(files) - file_id - 1
        for i, (free_start_pos, free_length) in enumerate(free):
            if start_pos < free_start_pos:
                break
            if free_length >= file_length:
                # move file
                files[file_id] = (free_start_pos, file_length)
                free[i] = (free_start_pos + file_length, free_length - file_length)
                break

    if len(files) <= 10:
        print(files)
        print_disk(files)
        print(free)

    return sum(
        pos * file_id
        for file_id, (start_pos, length) in enumerate(files)
        for pos in range(start_pos, start_pos + length)
    )


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
