# -*- coding:utf-8 -*-
# fb780098b6771f02c4682abea4d1d8cf
# 37.3505484 / 126.9442194
# json 데이터
# 검색어를 입력
#    => 위도/경도 지정
#    => 반경 1km이내에 있는 
#    => 검색어에 대한 위치 정보
from cx_Oracle import connect
from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads

#    => 장소명(업체명), 전화번호, 경도, 위도
#    => DB에 저장
#    => 전화번호 : 없는 부분은 ' - ' 으로 대체 
#    => 경도, 위도 : 소수점 6자리까지
# https://dapi.kakao.com/v2/local/search/keyword.${FORMAT}
with connect("lyh/1234@localhost:1521/xe") as con:
    cur = con.cursor()
    hc = HTTPSConnection("dapi.kakao.com")
    dict = {"Authorization": "KakaoAK fb780098b6771f02c4682abea4d1d8cf"}
    input = quote(input('장소 : '))
    hc.request("GET", f"/v2/local/search/keyword.json?x=37.3505484&y=126.9442194&radius=1000&query={input}", headers=dict)
    
    res = hc.getresponse()
    resBody = res.read()
    
    data = loads(resBody)
    for i in data['documents']:
        name = i['place_name']
        phone = i['phone']
        x = float(i['x'])
        y = float(i['y'])
        sql = f"insert into jul23_location values(jul23_location_seq.nextval, '{name}', "
        sql += f"nvl('{phone}', ' - '), {x:.6f}, {y:.6f})"
        cur.execute(sql)
    con.commit()  























































