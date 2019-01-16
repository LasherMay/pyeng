#!/usr/bin/env python3
access_dict = { 'FastEthernet0/17':150,
'FastEthernet0/10':10,
'FastEthernet0/12':12,
'FastEthernet0/7':110
}

def generate_access_config(access):
	result = []
	access_template = [
 'interface {}',
 'switchport mode access', 'switchport access vlan {}',
 'switchport nonegotiate', 'spanning-tree portfast',
 'spanning-tree bpduguard enable']
	for line in access:
		for lines in access_template:
			if lines.startswith('interface'):
				result.append(lines.format(line))
			elif 'vlan' in lines:
				result.append(lines.format(access[line]))
			else:
				result.append(lines)
	return print(result)

generate_access_config(access_dict)
#added for test
