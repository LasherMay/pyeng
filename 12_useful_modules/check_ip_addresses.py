#!/usr/bin/env python3.6
import subprocess

def check_ip_addresses(ip_address, count=2):
	'''
		Function gets a list of ip addresses and check if they are available or unavailable
		Check use ping command for every iteration in ip list
		First list is active hosts
		Second is disabled hosts
	'''
	active_hosts = []
	disabled_hosts = []
	for ipaddr in ip_address:
		reply = subprocess.run('ping -n {ip} -c {count}'.format(ip=ipaddr, count=count),
shell=True,stdout=subprocess.PIPE,
stderr=subprocess.PIPE,encoding='utf-8')
		if reply.returncode == 0:
			active_hosts.append(str(ipaddr))
		else:
			disabled_hosts.append(str(ipaddr))
	return active_hosts, disabled_hosts


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Ping to host script')
	parser.add_argument('host', action='store', help='IP to ping')
	parser.add_argument('-c', action='store', dest='count', type=int, help='Number of packets')
	args = parser.parse_args()
	print(args)
	check_ip_addresses(*args)

