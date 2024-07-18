# -*- coding:utf-8 -*-
from cx_Oracle import connect

# OracleDB와 연동이 되는 Java : instantClient ojdbc8.jar
# OracleDB와 연동이 되는 Python : cx_oracle.py(가 instantClient를 사용)

# 기본적으로 python에는 OracleDB연결 기능이 없어요...
# 시작 - cmd -> pip install cx_oracle
# pip list

# sqlplus로 접속할 때 사용하는 주소
#    sqlplus [ID]/[PW]@[IP Address]:[PORT]/[SID]
#    sqlplus lyh/1234@localhost:1521/xe
try:
    c = connect("lyh/1234@localhost:1521/xe")
    print('성공!')
except Exception as e:
    print(e)

c.close()

