# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

# http://openAPI.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/

hc = HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET", "/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/")

res = hc.getresponse()
res = res.read()
area = []
pm10 = []
pm25 = []
areaDictsum10 = {"도심권":0, "서북권":0, "동북권":0, "서남권":0, "동남권": 0}
areaDictsum25 = {"도심권":0, "서북권":0, "동북권":0, "서남권":0, "동남권": 0}
for i in loads(res)['RealtimeCityAir']['row']:
    area.append(i['MSRRGN_NM'])
    pm10.append(float(i['PM10']))
    pm25.append(float(i['PM25']))
    areaDictsum10[i['MSRRGN_NM']] += float(i['PM10']) 
    areaDictsum25[i['MSRRGN_NM']] += float(i['PM25']) 
pm10 = []
pm25 = []
for k, v in areaDictsum10.items():
    pm10.append(v / area.count(k))
for k, v in areaDictsum25.items():
    pm25.append(v / area.count(k))

area = ["도심권", "서북권", "동북권", "서남권", "동남권"]
plt.bar(area, pm10, color="#EB6B34")
plt.bar(area, pm25, color="#EB9F34", bottom=pm10)
plt.legend(["미세먼지", "초미세먼지"])
plt.show()
# 서북권, 도심권, 동북권, ... 의 미세먼지 / 초미세먼지
#    각각 평균값을 bar그래프로 표현 (누적합)




























































