#!/usr/bin/env python3
import sw_int_templates as sw_temp
from sw_data import sw1_fast_int
from sw_cfg_templates import basic_cfg, lines_cfg

def generate_access_cfg(sw_dict):
	result = []
	for intf, vlan in sw_dict['access'].items():
		result.append('interface FastEthernet' + intf)
		for command in sw_temp.access_template:
			if command.endswith('access vlan'):
				result.append(' {} {}'.format(command,vlan))
			else:
				result.append(' {}'.format(command))
	return result

print('\n'.join(generate_access_cfg(sw1_fast_int)))
