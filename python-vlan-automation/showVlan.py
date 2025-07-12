from netmiko import Netmiko
vlans=('')
device1 = {
"host" : '10.10.1.22',
'username' : 'admin',
'password' : '',
'device_type' : 'extreme_exos',
'global_delay_factor' : 0.1,
}
device2 = {
"host" : '10.10.1.24',
'username' : 'admin',
'password' : '',
'device_type' : 'extreme_exos',
'global_delay_factor' : 0.1,
}
device3 = {
"host" : '10.10.1.30',
'username' : 'admin',
'password' : '',
'device_type' : 'extreme_exos',
'global_delay_factor' : 0.1,
}
device4 = {
"host" : '10.10.1.31',
'username' : 'admin',
'password' : '',
'device_type' : 'extreme_exos',
'global_delay_factor' : 0.1,
}
device5 = {
"host" : '10.10.1.32',
'username' : 'admin',
'password' : '',
'device_type' : 'extreme_exos',
'global_delay_factor' : 0.1,
}
devicelist = (device1, device2, device3, device4, device5)

for device in devicelist:
	net_connect = Netmiko(**device)
	show_output = net_connect.send_command('show vlan description')
	net_connect.disconnect()
	print(show_output)
