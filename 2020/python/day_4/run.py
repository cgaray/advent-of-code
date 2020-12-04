#!/usr/bin/env python

import sys
from dataclasses import dataclass
from typing import get_type_hints, List
import re

import pdb

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
h_re = re.compile('#[a-f0-9]{6}')

@dataclass()
class Passport:
    byr: int = None
    iyr: int = None
    eyr: int = None
    hgt: int = None
    hgt_units: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None

    def __init__(self, passport_string: str):
        attr_dict = dict()
        for elem in passport_string.split():
            (field, value) = elem.split(':')
            if field == 'hgt':
                try:
                    setattr(self, 'hgt', int(value[:-2]))
                    setattr(self, 'hgt_units', value[-2:])
                except:
                    pass
            else:
                try:
                    setattr(self, field, get_type_hints(Passport)[field](value))
                except:
                    pass

    def val_byr(self):
        return len(str(self.byr)) == 4 and self.byr >= 1920 and self.byr <= 2002

    def val_iyr(self):
        return len(str(self.byr)) == 4 and self.iyr >= 2010 and self.iyr <= 2020

    def val_eyr(self):
        return len(str(self.byr)) == 4 and self.eyr >= 2020 and self.eyr <= 2030

    def val_hgt(self):
        return (self.hgt_units == 'in' and self.hgt >= 59 and self.hgt <= 76) or \
            (self.hgt_units == 'cm' and self.hgt >= 150 and self.hgt <= 193)

    def val_hcl(self):
        return h_re.match(self.hcl)

    def val_ecl(self):
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def val_pid(self):
        return len(self.pid) == 9

    def val_cid(self):
        return True

    def is_valid(self, required_fields = List[str]):
        for field in required_fields:
            if not getattr(self, field):
                return False
        return self.val_byr() and self.val_iyr() and self.val_eyr() and self.val_hgt() and self.val_hcl() and self.val_ecl() and self.val_pid() and self.val_cid()

def read_passports(filename):
    return open(filename, 'r').read().split('\n\n')

def main(filename):
    num_valid = 0
    for passport_string in read_passports(filename):
        p = Passport(passport_string)
        if p.is_valid(REQUIRED_FIELDS):
            num_valid += 1
        else:
            print(p)
    print(f"Number of valid passports: {num_valid}")
if __name__ == '__main__':
    filename = sys.argv[1]

    main(filename)
