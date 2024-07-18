# -*- coding:utf-8 -*-

# 파일로부터 데이터를 읽어와서 프로그램에서 활용하기 위함
# 프로그램에서 만든 데이터를 파일형태로 저장하기 위함

# 파일 열기 => 작업(읽기, 쓰기) => 파일 닫기 (필수 !!)

# .txt파일 / .csv (Comma Separated Value)파일

# 1. 파일에 내용 쓰기 (write)
# 폴더는 미리 만들어둬야함 / 파일은 존재하지 않아도 실행시 파일을 만들어줌
# C:\Users\sdedu\Desktop\file

# w : 덮어쓰기
# fileName = "file.txt" # 파일명.확장자
# file = open(f"C:/Users/sdedu/Desktop/file/{fileName}", "w", encoding="UTF-8") # mode : 어떤 모드를 활용 할 지 / # encoding ="utf-8"
# file.write("오늘 비가 겁나 오네요 ㅠㅠ 이따 점심 회식인데...") 
# print('완료!')
# file.close()

# 2. 파일에 내용을 추가 (append)
# a : 파일에 내용 추가
# fileName = "file.txt" # 파일명.확장자
# file = open(f"C:/Users/sdedu/Desktop/file/{fileName}", "a", encoding="UTF-8")
# file.write("\n오늘 제가 살아서 돌아온다면\n ~~~~~~~\n!@#!@#")
# print('완료!')
# file.close()

# 3. 파읽 읽어오기 (read)
# r : 파일 읽기
fileName = "file.txt" # 파일명.확장자
file = open(f"C:/Users/sdedu/Desktop/file/{fileName}", "r", encoding="UTF-8")

# 3-1. 파일 전체 읽기
# data = file.read()
# print(data)
# file.close()

# 3-2. 파일을 한줄씩 읽기
while True: # 내가 가져온 파일의 내용이 언제 끝날지 모르기 때문에 True
    data = file.readline() # 한 줄을 읽어옴
    print(data, end="")
    # readline의 결과가 공백인 상황(파일의 맨 마지막 줄까지 끝난 상황)
    if data == "": # 읽어온 줄이 공백이면 반복문 break!
        break
        
file.close()   
    




















































