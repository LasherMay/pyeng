#!/usr/bin/env python
import sys

(addString, cidrString) = sys.argv[1].split('/')

cidr = int(cidrString)
print(cidr)

print(addString)

ip = addString.split('.')

mask = cidr
mask_lost = (32 - mask) * '0'
mask = mask * '1'
mask = mask + mask_lost

mask = [mask[x:x+8] for x in range (0, len(mask) - len(mask) % 8, 8)]

ip_template = """
Network: 
{0:8} {1:8} {2:8} {3:8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
/{cidr}
{4:8} {5:8} {6:8} {7:8}
{4:08b} {5:08b} {6:08b} {7:08b}
"""

print(ip_template.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]),int(mask[0], 2),int(mask[1], 2),int(mask[2], 2), int(mask[3], 2),cidr=cidr))

