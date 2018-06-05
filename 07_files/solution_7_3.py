#!/usr/bin/env python3

template='{vlan:6}{mac:17}{intf:10}'

with open('CAM_table.txt') as s:
	table = []
	for line in s:
		split = line.split()
		if split == []:
			continue
		if split[0].isdigit():
			table.append(line)

for line in table:
	s = line.split()
	s.remove('DYNAMIC')
	vlan, mac, intf = s
	print(template.format(vlan=vlan,mac=mac,intf=intf))
