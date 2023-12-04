#!/usr/bin/python3
import requests
from sys import argv

email = {'email' : argv[2]}
response = requests.post(argv[1], data=email)
print(response.text)
