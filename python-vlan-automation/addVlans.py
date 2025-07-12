from netmiko import ConnectHandler
from getpass import getpass

password = getpass("Enter your SSH password: ")

devices = [
    {
        "host": "10.10.1.22",
        "username": "admin",
        "password": password,
        "device_type": "extreme_exos",
        "global_delay_factor": 0.1,
    },
    {
        "host": "10.10.1.30",
        "username": "admin",
        "password": password,
        "device_type": "extreme_exos",
        "global_delay_factor": 0.1,
    },
    {
        "host": "10.10.1.31",
        "username": "admin",
        "password": password,
        "device_type": "extreme_exos",
        "global_delay_factor": 0.1,
    },
    {
        "host": "10.10.1.32",
        "username": "admin",
        "password": password,
        "device_type": "extreme_exos",
        "global_delay_factor": 0.1,
    },
]

vlans = [
    {"vlan_id": 10, "vlan_name": "VLAN10"},
    {"vlan_id": 20, "vlan_name": "VLAN20"},
    {"vlan_id": 30, "vlan_name": "VLAN30"},
    {"vlan_id": 40, "vlan_name": "VLAN40"},
]


for device, vlan in zip(devices, vlans):
    try:
        print(f"Connecting to {device['host']}...")
        with ConnectHandler(**device) as net_connect:
    
            commands = [
                f"create vlan {vlan['vlan_name']} tag {vlan['vlan_id']}",
            ]
            
      
            output = net_connect.send_config_set(commands)
            print(f"Configuration output for {device['host']}:\n{output}")
            
           
            save_output = net_connect.save_config()
            print(f"Save configuration output for {device['host']}:\n{save_output}")
            
    except Exception as e:
        print(f"Failed to configure {device['host']}: {e}")

