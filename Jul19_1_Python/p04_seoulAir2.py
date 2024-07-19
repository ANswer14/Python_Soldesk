# -*- coding:utf-8 -*-
from cx_Oracle import connect

# DB에 있는 미세먼지 데이터 => csv에 저장(데이터 콤마로 구분)

file = open("C:/Users/sdedu/Desktop/file/file4.csv", "a", encoding="UTF-8")

con = connect("lyh/1234@localhost:1521/xe")
cur = con.cursor()
sql = "select * from jul19_seoul_air"

cur.execute(sql)
cur = cur.fetchall()
for no, name, pm10, pm25 in cur:
    file.write(f"{no},{name},{pm10},{pm25}\r\n")
con.close()
file.close()

print("성공")






















































