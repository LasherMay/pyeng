#!/usr/bin/env python3
def parse_cdp_neighbors(string):
	src_device = '''{}'''.format(string).split('\n')[0].split('>')[0]
	interfaces=('Fa', 'Eth', 'Gi')
	loi = '{}'.format(string).split('\n')	#list_of_input
	relations = {}
	for line in loi:
		if any(word in line for word in interfaces):
			rel = line.split()
			rel[4], rel[3] = rel[-1], rel[-2]
			dest_device, local_intf, local_intfnum, dest_intf, dest_intfnum, *other = rel
			relations[(src_device,local_intf+local_intfnum)] = (dest_device,dest_intf+dest_intfnum)
	return relations
