#!/usr/bin/env python3
from hashlib import md5
from itertools import count


def hashes(prefix):
    for i in count(start=1):
        yield i, md5(f'{prefix}{i}'.encode()).hexdigest()


def mine(prefix, zeroes):
    for i, h in hashes(prefix):
        if h[:zeroes] == '0' * zeroes:
            return i


def solve_part_1(prefix):
    return mine(prefix, 5)


def solve_part_2(prefix):
    return mine(prefix, 6)


if __name__ == "__main__":
    print(f'{solve_part_1("yzbqklnj")}, {solve_part_2("yzbqklnj")}')
