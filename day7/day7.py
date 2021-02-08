#!/usr/bin/env python3
import re


wiring, values = dict(), dict()

def get_value(w):
    if w in values:
        return values[w]

    wires = w.split(' ')
    if len(wires) == 1:
        val = int(wires[0]) if wires[0].isdigit() else get_value(wiring[wires[0]])
    elif len(wires) == 2:
        val = ~get_value(wires[1]) & 0xFFFF
    elif wires[1] == 'AND':
        val = get_value(wires[0]) & get_value(wires[2])
    elif wires[1] == 'OR':
        val = get_value(wires[0]) | get_value(wires[2])
    elif wires[1] == 'LSHIFT':
        val = get_value(wires[0]) << get_value(wires[2])
    elif wires[1] == 'RSHIFT':
        val = get_value(wires[0]) >> get_value(wires[2])
    else:
        val = None

    values[w] = val
    return val

def solve_part_1():
    return get_value('a')


def solve_part_2():
    wiring['b'] = str(get_value('a'))
    values.clear()
    return get_value('a')


if __name__ == "__main__":
    for ll in open('input.txt').readlines():
        l, r = ll.strip().split(' -> ')
        wiring[r] = l
    print(f'{solve_part_1()}, {solve_part_2()}')



