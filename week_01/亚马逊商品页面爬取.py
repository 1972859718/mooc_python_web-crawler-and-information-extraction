# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:30:53 2018

@author: moon
"""

import requests
url = "https://www.amazon.cn/gp/product/B07C9QR82G"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")