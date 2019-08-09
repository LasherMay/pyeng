#!/usr/bin/env python
import re


def filter_lines(filename, regex):
    with open(filename, 'r') as f:
        for line in f:
            if re.search(regex, line):
                yield line.rstrip()


for line in filter_lines('config_sw1.txt', '^interface'):
    print(line)
