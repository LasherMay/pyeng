#!/usr/bin/env python
import draw_network_graph
import solution11_1


draw_network_graph.draw_topology(solution11_1.parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))
