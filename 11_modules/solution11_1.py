#!/usr/bin/env python3
def parse_cdp_neighbors(string):
    src_device = '''{}'''.format(string).split('\n')[0].split('>')[0]
    interfaces=('Fa', 'Eth', 'Gi')
    loi = '{}'.format(string).split('\n') #list_of_input
    relations = {}
    for line in loi:
        if any(word in line for word in interfaces): #check if word in interfaces is in line
            dest_device, local_intf, local_intfnum, _, _, _, _, _, dest_intf, dest_intfnum = line.split()
            relations[(src_device,local_intf+local_intfnum)] = (dest_device,dest_intf+dest_intfnum)
    return relations
