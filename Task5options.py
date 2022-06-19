import requests

headers = {
    'Accept': 'application/yang-data+json',
}

response = requests.options('https://192.168.56.107:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity', headers=headers, verify=False, auth=('cisco', 'cisco123!'))
