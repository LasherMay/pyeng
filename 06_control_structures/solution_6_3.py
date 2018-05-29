#!/usr/bin/env python3

mode = input('Enter mode (access\\trunk): ')
access_template = ['switchport mode access',
'switchport access vlan ',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10',
'0/14':'11',
'0/16':'17',
'0/17':'150'},
		'trunk':{'0/1':['add','10','20'],
				'0/2':['only','11','30'],
				'0/4':['del','17']} }

if mode == 'access':
	for intf, vlan in fast_int[mode].items():
		print('interface FastEthernet' + intf)
		for command in access_template:
			if command.endswith('access vlan'):
				print(' {} {}'.format(command, vlan))
			else:
				print(' {}'.format(command))
elif mode == 'trunk':
	for intf, vlan in fast_int[mode].items():
		print('interface FastEthernet' + intf)
		for command in trunk_template:
			if command.endswith('allowed vlan'):
				if vlan[0] == 'add':
					print(' {} {}'.format(command,(','.join(vlan)).replace(',',' ')))
				elif vlan[0] == 'only':
					vlan.remove('only')
					print(' {} {}'.format(command,(','.join(vlan)).replace(',',' ')))
				elif vlan[0] == 'del':
					vlan.remove('del')
					vlan.insert(0,'remove')
					print(' {} {}'.format(command,(','.join(vlan)).replace(',',' ')))
				else:
					print('Enter correct command \'add\' \'only\' or \'del\'')
			else:
				print(' {}'.format(command))
else:
	print('Enter only access or trunk')
