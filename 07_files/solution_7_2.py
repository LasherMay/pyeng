#!/usr/bin/env python3
import sys

file = sys.argv[1]

with open(file, 'r') as f:
	for line in f:
		if line.startswith('!'):
			continue
		print(line.rstrip('\n'))

