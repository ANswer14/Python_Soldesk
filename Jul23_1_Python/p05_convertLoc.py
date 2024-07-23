# -*-coding:utf-8 -*-
from cx_Oracle import connect

# Table 데이터 => 번호값 제외한 모든 데이터 => csv파일 담는 작업
with open("C:/Users/sdedu/Desktop/file/file7.csv", "w", encoding="UTF-8") as f:
    with connect("lyh/1234@localhost:1521/xe") as con:
        cur = con.cursor()
        sql = "select l_name, l_phone, l_x, l_y from jul23_location"
        cur.execute(sql)
        for name, phone, x, y in cur:
            f.write(f"{name},{phone},{x},{y}\n")

























































