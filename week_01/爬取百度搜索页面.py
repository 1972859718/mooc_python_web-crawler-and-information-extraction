# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 13:45:06 2018

@author: moon
"""

import requests
keyword = "Python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")