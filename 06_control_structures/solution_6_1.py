#!/usr/bin/env python3

ipstr = input('Enter IP address like 10.0.0.0: ')
ip = int(ipstr.split('.')[0])
if ip >= 1 and ip <= 127:
	ipclass = ['A', 'unicast']
elif ip >= 128 and ip <= 191:
	ipclass = ['B','unicast']
elif ip >= 192 and ip <= 223:
	ipclass = ['C','unicast']
elif ip >= 224 and ip <= 239:
	ipclass = ['D','multicast']
elif ipstr == '0.0.0.0':
	ipclass = ['0.0.0.0','unassigned']
elif ipstr == '255.255.255.255':
	ipclass = ['255.255.255.255','local broadcast']
else:
	ipclass = [ipstr, 'unused']

print('Network class '+ ipclass[0] + ' with name ' + ipclass[1])
