access_template = ['switchport mode access',
		'switchpower access vlan {}',
		'switchport nonegotiate',
		'spanning-tree portfast',
		'spanning-tree bpduguard enable']
print('\n'.join(access_template).format(5))
