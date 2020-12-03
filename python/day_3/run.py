#!/usr/bin/env python

import sys
import pdb

START_POS = (0, 0) # upper left position
MOVE = (3, 1)      # right 3, down 1

def read_geography(filename):
    return open(filename, 'r').read().split()

def make_move(geography, pos, move):
    new_x = (pos[0] + move[0]) % len(geography[0])
    new_y = (pos[1] + move[1])

    if new_y > len(geography)-1:
        return None
    
    return (new_x, new_y)

def get_square(geography, pos):
    return geography[pos[1]][pos[0]]

def main(input_file):
    geography = read_geography(input_file)

    num_trees = 0
    cur_pos = make_move(geography, START_POS, MOVE)
    while cur_pos:
        if get_square(geography, cur_pos) == '#':
            num_trees += 1
        cur_pos = make_move(geography, cur_pos, MOVE)
    print(num_trees)


if __name__ == '__main__':
    input_file = sys.argv[1]

    main(input_file)