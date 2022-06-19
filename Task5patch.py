import requests

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
}

data = '{\n"native": {\n"logging": {\n"monitor": {\n"severity": "informational"\n}\n}\n}\n}'

response = requests.patch('https://192.168.56.107:443/restconf/data/Cisco-IOS-XE-native:native', headers=headers, data=data, verify=False, auth=('cisco', 'cisco123!'))