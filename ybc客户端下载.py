#This program is for download Prometheus(zh-CN:YuanBianCheng,猿编程) APP,COPYRIGHT (c) 2021 RYCB/BW Studio,ALL RIGHTS RESERVED.


import urllib.request as ur
import os


ur.urlretrieve('https://planet.fbcontent.cn/apps/download/yuanbiancheng-3.1.1.exe','ybc客户端安装程序.exe')
os.system('ybc客户端安装程序.exe')
