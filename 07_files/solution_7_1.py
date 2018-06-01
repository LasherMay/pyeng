#!/usr/bin/env python3

template = '''
Protocol: {:>15}
Prefix: {:>15}
AD/Metric: {:>15}
Next-Hop: {:>15}
Last update: {:>15}
Outbound Interface: {:>15}
'''

with open('ospf.txt') as src:
	for line in src:
		ospf = line.split()
		ospf.remove('via')
		s = [vlan.rstrip(',').strip('[]') for vlan in ospf]
		protocol, prefix, metric, nexthop, lastupdate, interface = s
		print(template.format(protocol, prefix, metric, nexthop, lastupdate, interface))
