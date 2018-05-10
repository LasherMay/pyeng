In [51]: command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'

In [52]: command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

In [53]: vlans = command1.split()[-1].split(',')+command2.split()[-1].split(',')

In [54]: vlans = [ int(vlan) for vlan in vlans if vlan.isdigit() ]

In [56]: vlans = list(set(vlans))

In [57]: vlans
Out[57]: [1, 3, 100, 200, 10, 300, 20, 30]
