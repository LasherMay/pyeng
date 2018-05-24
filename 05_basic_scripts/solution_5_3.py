#!/usr/bin/env python

mode = input('Enter interface mode (access/trunk): ')
intf = input('Enter interface type and number (e.g. Gi0/1): ')
vlans = input('Enter vlan(s) to add: ')


templates = { 'access_template' : 
'switchport mode access \nswitchport access vlan {vlans} \nswitchport nonegotiate \nspanning-tree portfast \nspanning-tree bpduguard enable\n',
'trunk_template' :
'switchport trunk encapsulation dot1q \nswitchport mode trunk \nswitchport trunk allowed vlan {vlans}'
}


print('\nInterface {}'.format(intf))
mode = mode + "_template"
print(templates[mode].format(vlans=vlans))
