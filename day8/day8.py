#!/usr/bin/env python3
import re


def decode(m):
    try:
        return chr(int(m.group(1)[1:], 16))
    except ValueError:
        return m.group(1)


def solve_part_1(lines):
    n_bytes = sum(len(l) for l in lines)
    n_char = 0
    for l in lines:
        d = re.sub(r'\\(?:(x[0-9a-f]{2}|[\\"]))', decode, l)
        n_char += len(d)
    return n_bytes - n_char + 2 * len(lines)


def solve_part_2(lines):
    n_chars = sum(len(l) for l in lines)
    n_encoded = 0
    for l in lines:
        n_encoded += len(l.replace('\\', '\\\\').replace('"', '\\"'))
    return n_encoded - n_chars + 2 * len(lines)


if __name__ == "__main__":
    lines = [ll.strip() for ll in open('input.txt').readlines()]
    print(f'{solve_part_1(lines)}, {solve_part_2(lines)}')
