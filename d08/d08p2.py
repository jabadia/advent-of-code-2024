from collections import defaultdict

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""", 34)
]


def solve(input):
    nodes = defaultdict(list)
    rows = input.strip().split('\n')
    for row in range(len(rows)):
        for col in range(len(rows[row])):
            if rows[row][col] != '.':
                frequency = rows[row][col]
                nodes[frequency].append((row, col))

    height = len(rows)
    width = len(rows[0])

    antinodes = set()
    for frequency, locations in nodes.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                node1 = locations[i]
                node2 = locations[j]
                offset = (node2[0] - node1[0], node2[1] - node1[1])

                n = 0
                while True:
                    antinode = (node1[0] + n * offset[0], node1[1] + n * offset[1])
                    if 0 <= antinode[0] < height and 0 <= antinode[1] < width:
                        antinodes.add(antinode)
                        n += 1
                    else:
                        break
                n = 0
                while True:
                    antinode = (node1[0] - n * offset[0], node1[1] - n * offset[1])
                    if 0 <= antinode[0] < height and 0 <= antinode[1] < width:
                        antinodes.add(antinode)
                        n += 1
                    else:
                        break

    return len(antinodes)


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
