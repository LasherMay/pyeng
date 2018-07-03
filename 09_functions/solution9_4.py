#!/usr/bin/env python3
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
	return any(word in command for word in ignore)

def config_to_dict(config):
	commands={}
	with open(config) as f:
		for line in f:
			if line.startswith('!') or line.startswith('\\'):
				pass
			elif ignore_command(line, ignore):
				pass
			elif not line.startswith(' '):
				buffer = line
				commands[buffer] = []
			elif line.startswith(' '):
				commands[buffer].append(line)
			else:
				print('Ti obosralsya')
		return print(commands)
