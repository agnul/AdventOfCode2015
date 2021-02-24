#!/usr/bin/env python3
import json
import re


def walk(node):
    if type(node) == int:
        return node
    elif type(node) == list:
        return sum(walk(n) for n in node)
    elif type(node) == dict:
        return sum(walk(n) for n in node.values()) if 'red' not in node.values() else 0
    else:
        return 0


def solve_part_1(input):
    return sum(map(int, re.findall(r'(-?\d+)', input)))


def solve_part_2(input):
    s = re.sub(r'{[^\[]*\"red\"[^[]*}', '0', input)
    return sum(map(int, re.findall(r'(-?\d+)', s)))

if __name__ == "__main__":
    input = open('input.txt').read()
    print(f'{solve_part_1(input)}, {solve_part_2(input)}')
