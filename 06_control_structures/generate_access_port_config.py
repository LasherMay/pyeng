#!/usr/bin/env python

access_template = ['switchport mode access',
'switchport access vlan',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

fast_int = {'access': { '0/12':10,
'0/14':11,
'0/16':17,
'0/17':150}}

for intf, vlan in fast_int['access'].items():
	print('interface FastEthernet' + intf)
	for command in access_template:
		if command.endswith('access vlan'):
			print(' {} {}'.format(command, vlan)
		else:
			print(' {}'.format(command))
