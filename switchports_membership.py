from netmiko import ConnectHandler
from switch_login import switch_login
from getpass import getpass

def switchports_membership():

    switchfile = input("Please enter filename where switches are listed:")
    vlan_id = input("Please enter vlan id:")
    username = input("Please enter username:")
    passwd = getpass()
    switchfile = open("switchfile.txt", "r")

    for switch in switchfile:
        net_connect = switch_login(switch, username, passwd)
        if net_connect != None:
#            print("Logged into switch : {}".format(switch))
            switch_command = "show interfaces status | i {}".format(vlan_id)
            output = net_connect.send_command(switch_command)
            print(output)
            print("\n\n")
        else:
            print("Something went wrong")
    switchfile.close()


if __name__ == "__main__":
    switchports_membership()