#!/usr/bin/env python
import sys

(addString, cidrString) = sys.argv[1].split('/')

cidr = int(cidrString)
print(cidr)

print(addString)
print(type(addString))

cidr = cidr * '1'
cidr_lost = (32 - cidr) * '0'
cidr = cidr + cidr_lost

print(cidr)
oktet=[]
for i in cidr:
	cidr[i] += cidr[i]
	if len(cidr[i]) % 7:
		oktet[i] = cidr[i]
		cidr[i-1] = ''

print(oktet)

ip_template = """
Network: 
{0:8} {1:8} {2:8} {3:8}
{0:8b} {1:8b} {2:8b} {3:8b}

Mask:
cidrString
{0:8} {1:8} {2:8} {3:8}
{0:8b} {1:8b} {2:8b} {3:8b}
"""


print(iptemplate.format(addString)
