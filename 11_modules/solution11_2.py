#!/usr/bin/env python3
import draw_network_graph
import solution11_1
a = '''SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
 R1           Eth 0/1         122           R S I           2811       Eth 0/0
 R2           Eth 0/2         143           R S I           2811       Eth 0/0
 R3           Eth 0/3         151           R S I           2811       Eth 0/0'''

draw_network_graph.draw_topology(solution11_1.parse_cdp_neighbors(a))
