#!/usr/bin/env python3
def get_int_vlan_map(config):
	access = {}
	trunk = {}
	with open(config) as f:
		for line in f:
			if 'interface Ethernet' in line:
				buffer = line.split()[-1]
			elif 'trunk allowed vlan' in line:
				a = line.split()[-1]
				trunk[buffer] = [int(s) for s in a.split(',')]
			elif 'access vlan' in line:
				access[buffer] = line.split()[-1]
	return access,trunk
