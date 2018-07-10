import subprocess
import argparse


def ping_ip(ip_address, count):
    '''
    Ping IP address and return tuple:
    On success: (return code = 0, command output)
    On failure: (return code, error output (stderr))
    '''
    reply = subprocess.run(
        'ping -c {count} -n {ip}'.format(count=count, ip=ip_address),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
		encoding='utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout + reply.stderr


parser = argparse.ArgumentParser(description='Ping script')

parser.add_argument('-a', action='store', dest='ip', required=True)
parser.add_argument('-c', action='store', dest='count', default=2, type=int)

args = parser.parse_args()
print(args)

rc, message = ping_ip(args.ip, args.count)
print(message)
