#!/usr/bin/env python

import sys
import itertools

def main(input_file):
    input = [int(elem) for elem in open(input_file, 'r').read().splitlines()]
    for (a, b) in itertools.combinations(input, 2):
        if a + b == 2020:
            print(a * b)

if __name__ == '__main__':
    input_file = sys.argv[1]
    
    main(input_file)