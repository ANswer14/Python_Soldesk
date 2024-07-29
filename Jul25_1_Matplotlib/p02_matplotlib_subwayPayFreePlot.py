# -*- coding:utf-8 -*-

# 방금 만든 csv 파일 불러와서
#    연월에 맞춰서 => 유임승차, 무임승차, 유임하차, 무임하차
#    => 선 그래프 그리기!

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
#
# fontFile = "C:/Windows/Fonts/malgun.ttf"
# fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
# plt.rc("")

with open("C:/Users/sdedu/Desktop/file/subway.csv", 'r', encoding="utf-8)") as f:
    data = f.readlines()
    oRD = {}
    nRD = {}
    oDD = {}
    nDD = {}
    for d in data:
        sData = d.split(",")
        data = sData[0]
        if data in oRD:
            oRD[f"{sData[0]}"] += int(sData[3])
            nRD[f"{sData[0]}"] += int(sData[4])
            oDD[f"{sData[0]}"] += int(sData[5])
            nDD[f"{sData[0]}"] += int(sData[6])
        else:
            oRD[f"{sData[0]}"] = int(sData[3])
            nRD[f"{sData[0]}"] = int(sData[4])
            oDD[f"{sData[0]}"] = int(sData[5])
            nDD[f"{sData[0]}"] = int(sData[6])
            
    date = []
    ord = []
    nrd = []
    odd = []
    ndd = []
    for k, v in oRD.items():
        date.append(k)
        ord.append(v)
        nrd.append(nRD[k])
        odd.append(oRD[k])
        ndd.append(nRD[k])
    month = 0
    list = []
    year = 2019
    for d in range(len(date)):
        month += 1
        if month == 13:
            month = 1
            year += 1
        list.append(f"{month}")

plt.plot(date, ord, "k:")


plt.plot(date, nrd, "g-")


plt.plot(date, odd, "b-.")
 
 
plt.plot(date, ndd, "y--")

plt.xticks(date, list)
plt.show()          
        
