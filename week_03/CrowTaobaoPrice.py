# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:56:24 2018

@author: moon
"""

#CrowTaobaoPrice.py
import requests
import re

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([title,price])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{0:4}\t{1:{3}<14}\t{2: >6}"
    print("爬取结果如下：\n")
    print(tplt.format("序号", "商品名称", "价格", chr(12288)))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1], chr(12288)))

def main():
    goods = '手机'
    #goods = str(input('请输入你想搜索的商品关键词：'))
    print("正在爬取商品信息，请稍后。。。\n")
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()