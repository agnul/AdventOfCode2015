#!/usr/bin/env python3
from itertools import combinations


def solve_part_1(packages):
    surface = 0
    for (l, w, h) in packages:
        surface += (2 * l * w + 2 * l * h + 2 * w * h)
        surface += min(map(lambda t: t[0] * t[1], combinations((l, w, h), 2)))
    return surface


def solve_part_2(packages):
    length = 0
    for (l, w, h) in packages:
        length += min(map(lambda t: 2 * t[0] + 2 * t[1], combinations((l, w, h), 2)))
        length += l * w * h
    return length


if __name__ == "__main__":
    packages = [(int(w), int(h), int(d)) for (w, h, d) in map(lambda l: l.split('x'), open('input.txt').readlines())]
    print(f'{solve_part_1(packages)}, {solve_part_2(packages)}')
