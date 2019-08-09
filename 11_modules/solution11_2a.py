#!/usr/bin/env python
import draw_network_graph
import solution11_1

list = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']

result_config = []
for i in list:
    with open(i) as f:
        for line in f:
            result_config.append(line.strip("\n"))
print(result_config)
with open('sum_config.txt', 'w') as sum:
    cfg_line = [ line + '\n' for line in result_config]
    sum.writelines(cfg_line)

draw_network_graph.draw_topology(solution11_1.parse_cdp_neighbors('sum_config.txt'), output_filename='img/sum_topology')