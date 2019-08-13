#!/usr/bin/env python
import re


line = '00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1'

match = re.search('(?P<mac>\S+)\s+(?P<ipaddr>\S+)\s+\d+\s+\S+\s+(?P<vlanid>\d+)\s+(?P<intf>\S+)', line)

print(match.groupdict())