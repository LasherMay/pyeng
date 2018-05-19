from sys import argv

interface = input('Введи имя интерфейса ')
vlan = input('Введи номер вилана ')

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

print('\n'+ '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
