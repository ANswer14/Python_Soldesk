# -*- coding:utf-8 -*-
# 활용 다 => 어필 O
from cx_Oracle import connect

# 원두를 검색해서 
# 그 원두를 사용하는 커피의 종류 갯수, 평균가를 출력
con = connect("lyh/1234@localhost:1521/xe")

cur = con.cursor()

bean = input('원두 : ')
sql = (f"select count(*), avg(c_price) from jul18_coffee where c_bean like '%{bean}%'")

cur.execute(sql)

data = cur.fetchall()

for c, p in data:
    # print(type(data))
    # print(data)
    # print(a)
    print(c, p)
    
con.close()




























































