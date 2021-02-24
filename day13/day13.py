#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations


def parse(filename):
    d = defaultdict(lambda: defaultdict(int))
    for ll in open(filename).readlines():
        pieces = ll.split()
        d[pieces[0]][pieces[-1][:-1]] = int(pieces[3]) if pieces[2] == 'gain' else -int(pieces[3])
    return d


def happiness(deltas, p):
    return sum(deltas[a][b] + deltas[b][a] for a, b in zip(p, p[1:] + (p[0], )))


def solve_part_1(deltas):
    return max(happiness(deltas, p) for p in permutations(deltas.keys()))


def solve_part_2(deltas):
    deltas['me'] = defaultdict(int)
    return max(happiness(deltas, p) for p in permutations(deltas.keys()))


if __name__ == "__main__":
    deltas = parse('input.txt')
    print(f'{solve_part_1(deltas)}, {solve_part_2(deltas)}')