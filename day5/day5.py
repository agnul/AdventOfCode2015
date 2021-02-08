#!/usr/bin/env python3
import re

def has_vowels(s):
    return sum(s.count(v) for v in 'aeiou') > 2 


def has_repeats(s):
    return any(d[0] == d[1] for d in zip(s, s[1:]))


def has_invalid(s):
    return any(seq in s for seq in ('ab', 'cd', 'pq', 'xy'))


def a_pair_repeats(s):
    return re.search(r'(..).*\1', s)


def a_letter_repeats(s):
    return re.search(r'(.).\1', s)


def is_nice(s, part_2=False):
    if part_2: 
        return a_pair_repeats(s) and a_letter_repeats(s)
    else:
        return has_vowels(s) and has_repeats(s) and not has_invalid(s)


def solve_part_1(strings):
    return len([s for s in strings if is_nice(s)])


def solve_part_2(strings):
    return len([s for s in strings if is_nice(s, True)])


if __name__ == "__main__":
    strings = [ll.rstrip() for ll in open('input.txt').readlines()]
    print(f'{solve_part_1(strings)}, {solve_part_2(strings)}')
