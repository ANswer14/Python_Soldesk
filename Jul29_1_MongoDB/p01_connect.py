# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient


# Python + MongoDB
# cmd => pip install pymongo
# 연결
con = MongoClient("192.168.0.33") # localhost도 가능!

db = con.jul29

con.close()
print("Success !")





















































