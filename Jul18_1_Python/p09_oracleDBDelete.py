# -*- coding:utf-8 -*-
from cx_Oracle import connect

# select 번호순으로 조회  => 번호를 입력하면 => 그 데이터가 삭제!
# 999를 입력하게 되면 프로그램이 종료 => 종료하기 전까지 반복

con = connect("lyh/1234@localhost:1521/xe")
cur = con.cursor()
while True:
    sql = "select * from jul18_coffee order by c_no"
    cur.execute(sql)
    data = cur.fetchall() 
    for n, n2, p, b in data:
        print(n, n2, p, b)
    delNum = int(input('삭제할 번호 입력 : '))
    if delNum == 999:
        break
    sql = f"delete from jul18_coffee where c_no = {delNum}"
    cur.execute(sql)
    if cur.rowcount == 1:
        con.commit()
con.close()
    
        























































