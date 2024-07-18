# -*- coding:utf-8 -*-
from cx_Oracle import connect

# input으로 숫자 2개를 입력 => 가격순(오름차순)으로 정렬해서
#                        => ? ~ ?번째까지의 평균가격을 출력

con = connect("lyh/1234@localhost:1521/xe")

cur = con.cursor()

num1, num2 = int(input('숫자 1 :')), int(input("숫자 2 :"))


sql = ("select round(avg(c_price), 2) from (")
sql +=("select rownum as rn, c_price from (")
sql +=("select c_price from jul18_coffee order by c_price desc ")
sql +=("))")
sql +=(f"where rn >= {num1} and rn <= {num2}")
cur = cur.execute(sql)
for p in cur: # cur 안에 tuple형태로 결과가 담김
    print(type(cur))
    print(p[0], type(p))


















































