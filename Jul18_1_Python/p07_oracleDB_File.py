# -*- coding:utf-8 -*-
from cx_Oracle import connect

# DB연결 => 커피이름, 가격, 원두 정보 => .csv파일로 생성(, 를 기준으로)
#    ex)    이름,가격,원두
#           이름,가격,원두
#            ...

con = connect("lyh/1234@localhost:1521/xe")

sql = ("select c_name, c_price, c_bean from jul18_coffee")

cur = con.cursor()
cur = cur.execute(sql)
cur = cur.fetchall()
file = open("C:/Users/sdedu/Desktop/file/file2.csv", "w", encoding="UTF-8")

for n,p,b in cur:
    file.write(f"{n},{p},{b}""\r\n")
    
# for t in cur:
    # file.write(str(t) + "\r\n")
file.close()



























































