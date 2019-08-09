#!/usr/bin/env python3
import re


def parse_cdp_neighbors(file):
	interfaces = ('Fa', 'Eth', 'Gi')
	relations = {}
	with open(file, 'r') as f:
		for line in f:
			print(line)
			src_device = re.search('^.+>', line)
			if src_device and not None:
				src_dev = src_device.group().rstrip('>')
			if any(word in line for word in interfaces):
				rel = line.split()
				rel[4], rel[3] = rel[-1], rel[-2]
				dest_device, local_intf, local_intfnum, dest_intf, dest_intfnum, *other = rel
				relations[(src_dev, local_intf + local_intfnum)] = (dest_device, dest_intf + dest_intfnum)
	return relations
