from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import SSHException
from switch_login import switch_login


def listports(switch, vlan, user, passwd):
    
    net_connect = switch_login(switch, user, passwd)
    if net_connect != None:
        output = net_connect.send_command("show interfaces status", use_textfsm = True)
        l = len(output)
        print("Below listed interafces are in vlan {}".format(vlan))
    
        for i in range(0,l):
            if output[i]['vlan'] == vlan:
                print("Interface {}".format(output[i]['port']))
           
if __name__ == '__main__':
    listports("inchsw-technical-01", "30", "inadhavv", "xyz")