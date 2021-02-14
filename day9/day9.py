#!/usr/bin/env python3
from itertools import permutations


def parse_input(fname):
    places, distances = set(), dict()
    for ll in open(fname).readlines():
        origin, _, destination, _, d = ll.split()
        places.add(origin)
        places.add(destination)
        distances[(origin, destination)] = int(d)
        distances[(destination, origin)] = int(d)
    return places, distances


def solve_part_1(places, distances):
    shortest = 999999999
    for p in permutations(places):
        dist = sum(distances[d] for d in zip(p[:-1], p[1:]))
        shortest = min(shortest, dist)
    return shortest


def solve_part_2(places, distances):
    longest = 0
    for p in permutations(places):
        dist = sum(distances[d] for d in zip(p[:-1], p[1:]))
        longest = max(longest, dist)
    return longest


if __name__ == "__main__":
    places, distances = parse_input('input.txt')
    print(f'{solve_part_1(places, distances)}, {solve_part_2(places, distances)}')
