#!/usr/bin/env python

import re
import sys
from collections import Counter

password_pattern = re.compile('(\d+)-(\d+)\s([a-z]):\s(\w+)')

def read_passwords(input_file):
    passwords = list()
    with open(input_file, 'r') as f:
        for line in f.read().splitlines():
            m = password_pattern.match(line)
            passwords.append([int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)])
    return passwords

def test_policy(password, policy_type):
    if policy_type == 'sled':
        c = Counter(password[3])
        test_result = c[password[2]] >= password[0] and c[password[2]] <= password[1]
    elif policy_type == 'toboggan':
        c = Counter([password[3][x-1] for x in (password[0], password[1])])
        test_result = c[password[2]] == 1
    else:
        print(f"Unrecognized password policy {policy_type}")
        sys.exit(1)

    return test_result

def main(input_file, policy_type):
    test_results = list()
    for password in read_passwords(input_file):
        test_results.append(test_policy(password, policy_type))
    print(sum(test_results))

if __name__ == '__main__':
    input_file = sys.argv[1]
    policy_type = sys.argv[2]
    
    main(input_file, policy_type)
