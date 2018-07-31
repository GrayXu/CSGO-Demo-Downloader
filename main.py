# coding: utf-8

# This is a CS:GO demo downloader
# Tested only on Chinese sever...

#  e.g."http://replay234.wmsj.cn/730/003264663068277211183_0194800244.dem.bz2"

import os
import sys
from urllib import request
import bz2
from bz2 import decompress


print("hello world!")

former = "http://replay234.wmsj.cn/730/"
latter = ".dem.bz2"

infoKeyList = []
nameList = []

list = os.listdir()
for i in list:
    if i.split('.')[-1] == "info":

        temp = i.split('_')
        infoKeyList.append(temp[1]+"_"+temp[2])
        nameList.append(i[:-5])

print("We would download "+str(len(infoKeyList))+" demo(s)")

for i in range(len(infoKeyList)):

    # download
    savePath = os.path.join(os.getcwd(), nameList[i]+".bz2")
    print("start downloading "+str(i+1))
    print(savePath)
    url = former + infoKeyList[i] + latter
    request.urlretrieve(url, savePath)
    print("end downloading "+str(i+1))

    # decompress
    print("start depressing "+str(i+1))
    newfilepath = os.path.join(os.getcwd(), nameList[i])
    print(newfilepath)
    zipfile = bz2.BZ2File(savePath)
    data = zipfile.read()
    open(newfilepath, 'wb').write(data)
    print("end depressing "+str(i+1))

print("The end")
