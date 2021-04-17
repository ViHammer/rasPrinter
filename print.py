import paramiko
from paramiko import SSHClient
from scp import SCPClient
import sys
import configparser


file = sys.argv[1]

config = configparser.ConfigParser()
config.read('config.ini')
name = config['credentials']['name']
password = config['credentials']['password']
ip = config['credentials']['ip']

ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
ssh.connect(hostname=ip, 
            port='22',
            username=name,
            password=password)


scp = SCPClient(ssh.get_transport())

scp.put(file, '/home/pi')

scp.close()