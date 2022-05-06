from getpass import getpass
from list_switches import list_switches
from listports import listports



def main():
    switch = input("Please enter core switch name:")
    vlan_id = input("Please enter vlan id:")
    username = input("Please enter username:")
    passwd = getpass()

    # Create List of all switches in the site
    dev_list = []
    dev_list = list_switches(switch, username, passwd, dev_list)
    dev_count = len(dev_list)

    #Now go through ech switch and pull out ports matching requested vlan
    for i in range(dev_count):
        listports(dev_list[i], vlan_id, username, passwd)


if __name__ == '__main__':
    main()