# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from cx_Oracle import connect
from json import loads

# http://openAPI.seoul.go.kr:8088
# /4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/

# 구 이름, 미세먼지, 초미세먼지의 정보를 DB에 담아주세요!
#    (여러 기간에 걸쳐 이 데이터를 모은다고 가정)

hc = HTTPConnection("openAPI.seoul.go.kr:8088")

hc.request("GET", "/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/")

res = hc.getresponse()
res = res.read()
con = connect("lyh/1234@localhost:1521/xe")
cur = con.cursor()
dateSet = {0}
seoulData = loads(res)
# for s, v in enumerate(seoulData['RealtimeCityAir']['row']):
    # sql = "select * from jul19_seoul_air"
    # cur.execute(sql)
    # data = cur.fetchall()
    # for n, d, name, pm10, pm25 in data:
        # dateSet.add(d)
    # print(dateSet)
    # date = seoulData['RealtimeCityAir']['row'][s]['MSRDT']
    # if  date not in dateSet:
        # name = seoulData['RealtimeCityAir']['row'][s]['MSRSTE_NM']
        # pm10 = seoulData['RealtimeCityAir']['row'][s]['PM10']
        # pm25 = seoulData['RealtimeCityAir']['row'][s]['PM25']
        # sql = f"insert into jul19_seoul_air values(jul19_seoul_air_seq.nextval, to_date('{date}', 'YYYYMMDDHH24MI'), '{name}', {pm10}, {pm25})"
        # cur.execute(sql)
        # print('성공!')
for a in seoulData["RealtimeCityAir"]["row"]:
    sql = f"insert into jul19_seoul_air values(jul19_seoul_air_seq.nextval, "
    sql += f"'{a['MSRSTE_NM']}', {a['PM10']}, {a['PM25']})"
    cur.execute(sql)
con.commit()
con.close()
















































