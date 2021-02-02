#!/usr/bin/env python3

def solve_part_1(data):
    floor = 0
    for c in data:
        floor += (1 if c == '(' else -1)
    return floor


def solve_part_2(data):
    floor = 0
    for i, c in enumerate(data, start=1):
        floor += (1 if c == '(' else -1)
        if floor == -1:
            return i


if __name__ == "__main__":
    data = open('input.txt').readline().rstrip()
    print(f'{solve_part_1(data)}, {solve_part_2(data)}')
