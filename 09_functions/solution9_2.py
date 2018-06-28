#!/usr/bin/env python3
trunk_dict = { 'FastEthernet0/1':[10,20,30],
'FastEthernet0/2':[11,30],
'FastEthernet0/4':[17] }

def generate_trunk_config(trunk):
	result = []
	trunk_template = ['interface {}',
'switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan {}']
	for interface in trunk:
		for line in trunk_template:
			if 'interface' in line:
				result.append(line.format(interface))
			elif 'vlan' in line:
				result.append(line.format(', '.join([str(i) for i in trunk[interface]])))
			else:
				result.append(line)
	return print(result)

generate_trunk_config(trunk_dict)
