#!/usr/bin/python3
"""script that takes your github credentials and uses the github
api to display your id"""


import requests
from sys import argv

username = argv[1]
password = argv[2]

r = requests.get('https://api.github.com/users/{}'.format(username), auth=(username, password))
r_dict = r.json()

print(r_dict['id'])
