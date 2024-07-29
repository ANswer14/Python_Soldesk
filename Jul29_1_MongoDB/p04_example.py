# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from http.client import HTTPConnection
from json import loads

# http://openAPI.seoul.go.kr:8088
# /4f626857416f6c6c3632586a416843/json/SearchParkInfoService/1/132/

# 전체 공원 데이터 중에
#    공원이름 (PK), 공원 소개, 개원일, 주소 
#    => MongoDB에 넣고

# 다 넣었으면 => 출력 (console)
con = MongoClient('localhost')
hc = HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET", "/4f626857416f6c6c3632586a416843/json/SearchParkInfoService/1/132/")

db = con.jul29


resBody = hc.getresponse().read()

# for i in loads(resBody)["SearchParkInfoService"]['row']:
    # db.jul29_park.insert_one({ "_id" : i['P_PARK'], "introduce" : i["P_LIST_CONTENT"], "open" : i["OPEN_DT"], "addr" : i["P_ADDR"]})

for l in db.jul29_park.find():
    print(l["_id"])
    print(l["introduce"])
    if l["open"] == "":
        print(" - ")
    else: 
        print(l["open"])
    print(l["addr"])
    print('------------------------')

con.close()
























































