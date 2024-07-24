# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/1/5/20151101/

# 2021 ~ 2023 3년치 데이터를
# 연, 월, 일, 노선번호, 정류장명(역명), 승차총승객수, 하차총승객수
# 연도별로 csv파일에 저장

# 정류장명(역명) => 혹시 ,가 들어있을수도 있으니
#        => , 를 . 로 바꿔서 저장

# 인원수 관련 => 정수형태로 저장
hc = HTTPConnection("openapi.seoul.go.kr:8088")
first = 1
last = 1000
year = 2022
month = 1
day = 1
while True:
    if last == 41000:
        first = 1
        last = 1000
        day += 1
        if day == 31:
            day = 1
            month += 1
    if month < 10 and day < 10:
        hc.request("GET", f"/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/{first}/{last}/{year}0{month}0{day}/")
    elif month < 10 and day >= 10:
        hc.request("GET", f"/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/{first}/{last}/{year}0{month}{day}/")
    elif month >= 10 and day < 10:
        hc.request("GET", f"/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/{first}/{last}/{year}{month}0{day}/")
    else: 
        hc.request("GET", f"/4f626857416f6c6c3632586a416843/json/CardBusStatisticsServiceNew/{first}/{last}/{year}{month}{day}/")
    resBody = hc.getresponse().read()
    first += 1000
    last += 1000
    if "RESULT" in loads(resBody):
        continue
    with open("C:/Users/sdedu/Desktop/file/2022.csv", "a", encoding="UTF-8") as f:
        for i in loads(resBody)["CardBusStatisticsServiceNew"]['row']:
            no = i['RTE_NO']
            name = i["SBWY_STNS_NM"].replace(",", ".")
            rise = str(int(i["GTON_TNOPE"]))
            descend = str(int(i["GTOFF_TNOPE"]))
            f.write(f"{year},{month},{day},{no},{name},{rise},{descend}\n")
    if month == 12 and day == 31 and last == 41000:
        break









































