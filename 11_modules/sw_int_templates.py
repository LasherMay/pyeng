#!/usr/bin/env python3
access_template = ['switchport mode access',
'switchport access vlan',
'spanning-tree portfast',
'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan']
l3int_template = ['no switchport', 'ip address']
