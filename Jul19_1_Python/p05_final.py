# -*- coding:utf-8 -*-
from cx_Oracle import connect
from datetime import datetime

# 메뉴만들기 (함수) 
# 1. 학생 등록 / 2. 강의장 조회 / 3. 학생 조회 / 4. 학생정보를 파일로 내보내기
# 0. 종료

# 강의장 조회 : 1강의장 - 6층 복도 오른쪽
# 학생 조회 : 이름, 생년월일(연-월-일 (요일)), 나이, 몇 강의장
#            중간 점수, 기말 점수, 평균 점수
# 파일로 내보내기 (학생의 전체 정보 다 csv파일로)

def regStudent():
    print('학생 등록 창입니다~')
    name = input('학생 이름 : ')
    birthday = input('생년월일(연-월-일) :')
    inputClass = int(input('강의장 (몇 강의장?): '))
    middleScore = int(input('중간 점수 : '))
    finalScore = int(input('기말 점수 : '))
    sql =f"insert into jul19_student values(jul19_student_seq.nextval, '{name}', to_date('{birthday}', 'YYYY-MM-DD'), {inputClass}, {middleScore}, {finalScore})"
    cur.execute(sql)
    if cur.rowcount == 1:
        print('성공!')
        con.commit()
    else:
        print('실패!')
    con.close()  
def showClass():
    print('강의장 조회 창입니다~')
    sql = f"select * from jul19_class"
    cur.execute(sql)
    for c in cur:
        print(c)
    con.close()
def showStudent():
    print('학생 조회 창입니다~')
    sql = f"select * from jul19_student"
    cur.execute(sql)
    
    for _, name, date, iClass, middle, final in cur:
        age = datetime.now().year - date.year
        stdScore = (int(middle) + int(final)) / 2
        print(f"이름 : {name} ||생년월일 {date:%Y-%m-%d}({date:%A}) || 나이 : {age} || 강의장 : {iClass} || 중간 : {middle} || 기말 : {final} || 평균 : {stdScore}\r\n")
    con.close()
def getFileStudentInfo():
    file = open("C:/Users/sdedu/Desktop/file/file5.csv", "w", encoding="UTF-8")
    sql = f"select * from jul19_student"
    cur.execute(sql)
    for _, name, date, iClass, middle, final in cur:
        age = datetime.now().year - date.year
        stdScore = (int(middle) + int(final)) / 2
        file.write(f"이름 : {name},생년월일 {date:%Y-%m-%d} ({date:%A}),나이 : {age}, 강의장 : {iClass}, 중간 : {middle}, 기말 : {final}, 평균 : {stdScore}\r\n")
    file.close()
    
def start():
    while True:
        print('||1. 학생 등록||2. 강의장 조회||3. 학생 조회||4. 학생정보를 파일로 내보내기||0. 종료')
        select = int(input('번호 입력 : '))
        if select == 1:
            regStudent()
        elif select == 2:
            showClass()
        elif select == 3:
            showStudent()
        elif select == 4:
            getFileStudentInfo()
        elif select == 0:
            print('종료!')
            break
        else:
            print('잘못 입력 !!')
    
if __name__=="__main__":
    con = connect("lyh/1234@localhost:1521/xe")
    cur = con.cursor()
    start()














































