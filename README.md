## Switchports VLAN locator

### Introduction:
1. This is simple project to locate switchports that belong to a given vlan.
2. You just need to give core switch details and program will run through all switches to find all ports in given VLAN.
3. This code uses recursion to discover entire switch topology using core switch.

### Dependancies:
1. Install modules mentioned in requirements file.
`pip install -r requirements.txt`
2. Download folder from https://github.com/networktocode/ntc-templates
3. Add envirnment veriable to system with below name and value:

`Name - NET_TEXTFSM`
`Value - folder_path\ntc-templates\templates`