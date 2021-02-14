#!/usr/bin/env python3

def look_and_say(string):
    i, say = 0, ''
    while i < len(string):
        j = i
        while j < len(string) and string[i] == string[j]:
            j += 1
        say += str(j - i) + string[i]
        i = j
    return say


def play(string, rounds):
    next = string
    for _ in range(rounds):
        next = look_and_say(next)
    return next


def solve_part_1(string):
    return len(play(string, 40))


def solve_part_2(string):
    return len(play(string, 50))


if __name__ == "__main__":
    print(f'{solve_part_1("1321131112")}, {solve_part_2("1321131112")}')
