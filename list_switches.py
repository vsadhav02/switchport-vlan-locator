from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import SSHException
from switch_login import switch_login


def list_switches(switch, user, passwd, device_list):
    net_connect = switch_login(switch, user, passwd)
    if net_connect != None:
        output = net_connect.send_command("show cdp neighbors", use_textfsm = True) 
        l = len(output)
        

        for i in range(0,l):
            if output[i]["platform"][:2] == "WS":
                device = output[i]["neighbor"].split('.')[0]
                if device not in device_list:
                    device_list.append(device)
                    device_list = list_switches(device, user, passwd, device_list)
        
    return device_list


if __name__ == '__main__':
    device_list = []
    device_list = list_switches("inchsw-core-01", "inadhavv", "xyz", device_list)
    print(device_list)