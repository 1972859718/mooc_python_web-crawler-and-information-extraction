# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:21:29 2018

@author: moon
"""

import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"
if __name__ == "__main__":
    url = "https://item.jd.com/6949475.html"
    print(getHTMLText(url))