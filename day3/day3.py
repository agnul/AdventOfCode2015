#!/usr/bin/env python3
directions = {
    '^': ( 0,  1),
    '>': ( 1,  0),
    'v': ( 0, -1),
    '<': (-1,  0)
}


def solve_part_1(input):
    visited, current = {(0, 0)}, (0, 0)
    for d in input:
        delta = directions[d]
        current = (current[0] + delta[0], current[1] + delta[1])
        visited.add(current)
    return len(visited)


def solve_part_2(input):
    visited = {(0, 0)}
    santa, robot = (0, 0), (0, 0)
    for i, d in enumerate(input):
        delta = directions[d]
        if i % 2 == 0:
            santa = (santa[0] + delta[0], santa[1] + delta[1])
            visited.add(santa)
        else:
            robot = (robot[0] + delta[0], robot[1] + delta[1])
            visited.add(robot)
    return len(visited)


if __name__ == "__main__":
    input = open('input.txt').readline().rstrip()
    print(f'{solve_part_1(input)}, {solve_part_2(input)}')
