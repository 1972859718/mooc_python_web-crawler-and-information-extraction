# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:27:05 2018

@author: moon
"""

import requests
url = "http://www.ip138.com/ips138.asp?ip="
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-2200:-1800])
    print(len(r.text))
except:
    print("爬取失败")