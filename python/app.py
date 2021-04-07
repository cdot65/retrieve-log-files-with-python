from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

key_file='/home/cremsburg/.ssh/id_rsa'
syslog='./device_logs.log'

device_connection = Device('dallas-fw0', ssh_private_key_file=key_file)
with SCP(device_connection, progress=True) as scp:
    scp.get('/var/log/messages', local_path=syslog)
