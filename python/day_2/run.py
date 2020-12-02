#!/usr/bin/env python

import sys
from collections import Counter

def read_passwords(input_file):
    passwords = list()
    with open(input_file, 'r') as f:
        for line in f.read().splitlines():
            (policy_parts, password) = line.split(':')

            range_parts = policy_parts.split(' ')[0]

            policy = {
                'min'      : int(range_parts.split('-')[0]),
                'max'      : int(range_parts.split('-')[1]),
                'character': policy_parts.split(' ')[1]
            }

            passwords.append(
                {
                    'policy'  : policy,
                    'password': password.strip()
                }
            )
    return passwords

def test_policy(policy, password):
    c = Counter(password)
    
    return c[policy['character']] >= policy['min'] and c[policy['character']] <= policy['max']

def main(input_file):
    test_results = list()
    for password in read_passwords(input_file):
        test_results.append(test_policy(password['policy'], password['password']))
    print(sum(test_results))

if __name__ == '__main__':
    input_file = sys.argv[1]
    
    main(input_file)
