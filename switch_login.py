from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import SSHException

def switch_login(switch, user, passwd):
    SWT = {
        'device_type': 'cisco_ios',
        'ip': switch,
        'username': user,
        'password': passwd
    }

    print("connecting to device:{} .....".format(switch))

    try:
        net_connect = ConnectHandler(**SWT)
    except NetMikoTimeoutException:
        print("Device is not reachable")
        return None

    except NetMikoAuthenticationException:
        print("Authentication Failure")
        return None

    except SSHException:
        print("Make sure SSH is enabled")
        return None

    return net_connect


if __name__ == "__main__":
    switch_login("inchsw-canteen-01", "inadhavv", "xyz")