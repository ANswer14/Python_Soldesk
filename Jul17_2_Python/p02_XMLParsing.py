# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# https://openapi.naver.com/v1/search/shop.xml
# 83aibXx8mGY5VUSuU9oJ
# H6_BpJ3jun

# 상품명 : 입력
# xml 파싱해서 
# 문서의 제목 / 최저가 / 브랜드 / 대분류 카테고리 정보를 출력


q = input('상품명 : ')

# URLEncoding해서 주소로 넘겨줄 것
# urllib.parse
q = quote(q)

def cut(t):
    t = t.replace("<b>", "").replace("</b>", "")
    return t

hc = HTTPSConnection("openapi.naver.com")
dict = {"X-Naver-Client-Id":"83aibXx8mGY5VUSuU9oJ",
        "X-Naver-Client-Secret":"H6_BpJ3jun"}
hc.request("GET", "/v1/search/shop.xml?query=" + q, headers=dict)  
res = hc.getresponse()
resBody = res.read()

p = fromstring(resBody)
for w in p.iter("item"):
    print(w.find("title").text.replace("<b>", "").replace("</b>", ""))
    print(w.find("lprice").text)
    print(w.find("brand").text)
    for c in range(3):
        print(w.find(f"category{c + 1}").text)
    print('-----------------------')






