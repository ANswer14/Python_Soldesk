# -*- coding:utf-8 -*-
from cx_Oracle import connect

# csv파일로 만들어주세요! (번호, 시간, 온도, 최고기온, 날씨, 바람속도의 형태로)

file = open("C:/Users/sdedu/Desktop/file/file3.csv", "w", encoding="UTF-8")

con = connect("lyh/1234@localhost:1521/xe")
cur = con.cursor()

sql = "select * from jul19_weather"

cur.execute(sql)
data = cur.fetchall()
for n, t, t2, tm, w, w2 in data:
    # file.write(str(n) +", " + str(t) + ", " + str(t2) + ", " + str(tm) + ", " + w + ", " + w2 +"\r\n")
    file.write(f"{n},{t},{t2},{tm},{w},{w2}\r\n")
con.close()
file.close()
























































