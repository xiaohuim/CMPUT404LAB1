#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get('http://www.google.ca')
print response.status_code
print response.text
