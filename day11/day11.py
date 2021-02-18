#!/usr/bin/env python3
import re

from itertools import count


def atoi(s):
    i = 0
    for c in s:
        i = i * 26 + ord(c) - ord('a')
    return i


def itoa(n):
    s = ''
    while n:
        s = chr(n % 26 + ord('a')) + s
        n //= 26
    return str.rjust(s, 8, 'a')


def is_straight(s):
    return ord(s[0]) == (ord(s[1]) - 1) == (ord(s[2]) - 2)


def has_straight(s):
    return any(is_straight(s[i:i+3]) for i in range(len(s) - 3))


def no_ilo(s):
    return 'i' not in s and 'l' not in s and 'o' not in s


def has_repeats(s):
    return bool(re.search(r'((.)\2.*){2,}', s))


def is_good(s):
    return has_straight(s) and no_ilo(s) and has_repeats(s)


def solve_part_1(p):
    for i in count(start=atoi(p)+1):
        if is_good(itoa(i)): return itoa(i)


def solve_part_2(p):
    return solve_part_1(solve_part_1(p))


if __name__ == "__main__":
    print(f'{solve_part_1("cqjxjnds")}, {solve_part_2("cqjxjnds")}')
