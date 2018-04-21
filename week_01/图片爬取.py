# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 13:59:56 2018

@author: moon
"""

import requests
import os
url = "http://img.netbian.com/file/2018/0416/b431c72c180e5eaf4ccb383cf4c0ec3c.jpg"
root = "D://Users//moon//Desktop//"
path = root + url.split('e')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
            print("文件已存在")
except:
    print("爬取失败")