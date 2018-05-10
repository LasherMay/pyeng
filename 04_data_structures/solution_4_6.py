In [48]: ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [49]: template = '''
    ...: Protocol: {:>15}
    ...: Prefix: {:>15}
    ...: AD/Metric: {:>15}
    ...: Next-Hop: {:>15}
    ...: Last update: {:>15}
    ...: Outbound Interface: {:>15}
    ...: '''

In [50]: ospf = ospf_route.split()

In [51]: ospf.remove('via')

In [52]: ospf = [ vlan.rstrip(',').strip('[]') for vlan in ospf ]

In [53]: protocol, prefix, metric, nexthop, lastupdate, interface = ospf

In [54]: print(template.format(protocol, prefix, metric, nexthop, lastupdate, interface))

   ...: Protocol:               O
   ...: Prefix:    10.0.24.0/24
   ...: AD/Metric:          110/41
   ...: Next-Hop:       10.0.13.3
   ...: Last update:           3d18h
   ...: Outbound Interface: FastEthernet0/0
