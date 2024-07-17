# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring


# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4141051000
# HTTP 통신 
hc = HTTPSConnection("www.kma.go.kr")       # 서버 주소(http라면 HTTPConnection 으로!!)
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4141051000")   # 요청

res = hc.getresponse()  # 응답
resBody = res.read()    # 응답 내용
# print(resBody)
# print(resBody.decode()) # 출력(한글처리)
#########################################################
# XML Parsing    
# DOM객체 여러개 찾기 : .getiterator("태그명") / .iter("태그명")
# DOM객체 하나 찾기 : .find("태그명")

kmaWeateher = fromstring(resBody)
print(kmaWeateher)
# weathers = kmaWeateher.iter("data")
# # print(weathers)
# for w in weathers:
    # print(w)
    # print('-----------------------')
for w in fromstring(resBody).getiterator("data"): # .iter 들어가도 상관 X
    print(w.find("hour").text)
    print(w.find("temp").text)
    print(w.find("wfKor").text)
    print('--------------')





















































