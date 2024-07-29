# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/CardSubwayPayFree/1/5/201501/

# 2019 ~ 2023년 월별로 > 하나의 파일(csv)에 저장
# 연월(ex:201901), 호선명, 지하철역, 유임승차인원, 무임승차인원, 유임하차인원, 무임하차인원

hc = HTTPConnection("openapi.seoul.go.kr:8088")
month = 1
year = 2019
first = -999
last = 0
while True:
    if last == 2000:
        first = -999
        last = 0
        month += 1
    if month == 13:    
        month = 1
        year += 1
    if year == 2024:
        break
    first += 1000
    last += 1000
    if month < 10:
        hc.request("GET", f"/4f626857416f6c6c3632586a416843/json/CardSubwayPayFree/{first}/{last}/{year}0{month}/")
    else:
        hc.request("GET", f"/4f626857416f6c6c3632586a416843/json/CardSubwayPayFree/{first}/{last}/{year}{month}/")
    resBody = hc.getresponse().read()
    f = open("C:/Users/sdedu/Desktop/file/subway.csv", "a", encoding='UTF-8')
    if "CardSubwayPayFree" not in loads(resBody):
        continue
    for i in loads(resBody)["CardSubwayPayFree"]["row"]:
        name = i["SBWY_ROUT_LN_NM"]
        station = i["STTN"]
        p1 = int(i["RMIO_GTON_NOPE"])
        p2 = int(i["FREECHRG_GTON_NOPE"])
        p3 = int(i["RMIO_GTOFF_NOPE"])
        p4 = int(i["FREECHRG_GTOFF_NOPE"])
        if month < 10:
            f.write(f"{year}0{month},{name},{station},{p1},{p2},{p3},{p4}\n")
        else:
            f.write(f"{year}{month},{name},{station},{p1},{p2},{p3},{p4}\n")
f.close()