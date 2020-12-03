#!/usr/bin/env python

import sys
from itertools import combinations
from math import prod

def main(input_file, combo_length):
    input = [int(x) for x in open(input_file).read().split()]
    for combo in combinations(input, combo_length):
        if sum(combo) == 2020:
            print(prod(combo))
            sys.exit(0)

if __name__ == '__main__':
    input_file = sys.argv[1]
    combo_length = int(sys.argv[2])
    
    main(input_file, combo_length)