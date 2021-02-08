#!/usr/bin/env python3
import re 

from collections import defaultdict

def parse_line(ll):
    op, x1, y1, x2, y2 = re.findall(r'(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)', ll)[0]
    return (op, (int(x1), int(y1)), (int(x2), int(y2)))


def solve_part_1(instructions):
    lights = dict()
    for op, a, b in instructions:
        for x in range(a[0], b[0] + 1):
            for y in range(a[1], b[1] + 1):
                if op == 'on':
                    lights[(x, y)] = 1
                elif op == 'off':
                    lights[(x, y)] = 0
                elif lights.get((x, y), 0) == 1:
                    lights[(x,y)] = 0
                else:
                    lights[(x,y)] = 1
    return sum(lights.values())


def solve_part_2(instructions):
    lights = defaultdict(int)
    for op, a, b in instructions:
        for x in range(a[0], b[0] + 1):
            for y in range(a[1], b[1] + 1):
                if op == 'on':
                    lights[(x, y)] += 1
                elif op == 'off':
                    lights[(x, y)] = max(0, lights[(x, y)] - 1)
                else:
                    lights[(x,y)] += 2
    return sum(lights.values())


if __name__ == "__main__":
    instructions = [parse_line(ll) for ll in open('input.txt').readlines()]
    print(f'{solve_part_1(instructions)}, {solve_part_2(instructions)}')
