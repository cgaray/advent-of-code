#!/usr/bin/env python

import sys
import itertools
import math

def main(input_file, combo_length):
    input = [int(elem) for elem in open(input_file, 'r').read().splitlines()]
    for combo in itertools.combinations(input, combo_length):
        if sum(combo) == 2020:
            print(math.prod(combo))
            sys.exit(0)

if __name__ == '__main__':
    input_file = sys.argv[1]
    combo_length = int(sys.argv[2])
    
    main(input_file, combo_length)