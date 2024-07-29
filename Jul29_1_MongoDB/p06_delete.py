# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("localhost")

db = con.jul29

# remove() / delete_one() + delete_many()
# db.jul29_lunch.remove({"_id" : "test"}) => ( in cmd )
# db.jul29_lunch.remove({}) => mongoDB cmd 내에서 전체 데이터 삭제 시

# 해당 데이터 하나만 삭제
db.jul29_lunch.delete_one({"price": 8000}) # 처음에만 적용 (multi:False)

# 해당 데이터 전체 삭제
db.jul29_lunch.delete_many({"price" : 8000}) # 모두 적용 (multi:True)
db.jul29_lunch.delete_many({}) # == (in cmd) db.jul29_lunch.remove({})

con.close()
print('Success !')












































