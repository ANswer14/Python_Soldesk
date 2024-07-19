# -*- coding:utf-8 -*-
from cx_Oracle import connect
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# 기상청 (주소값 구해서)
# 기상청 xml => DB에 적재
# 시간대 / 기온 / 최고기온 / 날씨(한글) / 풍향(한글)
# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4141051000
hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4141051000")
con = connect("lyh/1234@localhost:1521/xe")
cur = con.cursor()

res = hc.getresponse()
res = res.read()

for w in fromstring(res).iter("data"):
    hour = w.find("hour").text 
    temp = w.find("temp").text
    tmx = w.find("tmx").text
    wfKor = w.find("wfKor").text
    wdKor = w.find("wdKor").text
    sql = f"insert into jul19_weather values(jul19_weather_seq.nextval, {hour}, {temp}, {tmx}, '{wfKor}', '{wdKor}')"
    cur.execute(sql)
    
con.commit()
con.close()





























































