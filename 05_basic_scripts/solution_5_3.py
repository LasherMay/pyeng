#!/usr/bin/env python

mode = input('Enter interface mode (access/trunk): ')
intf = input('Enter interface type and number (e.g. Gi0/1): ')
vlan = input('Enter vlan(s) to add: ')


access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']

print('Interface {}\n'.format(intf))
choice = {}_template.format(mode)
print(choice)
