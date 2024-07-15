# -*- coding:utf-8 -*-
from random import randint
import random

# 숫자야구 (3자리) (함수) (각 자릿수의 숫자는 중복 X)
# 012 ~ 987 중에 랜덤한 숫자 정답 (각 자리의 값들은 list에 담기)
# 유저가 입력 => 자릿수와 값까지 같으면 S, 자릿수는 다른게 값이 같으면 B
# S가 3개 나오면 정답! => 종료

def getNum():
    list = []
    for i in range(3):
        ran = random.randint(0, 9)
        for j in range(len(list)):
            if ran in list:
                while ran in list:
                    ran = randint(0, 9)
        list.append(ran)
    
    return list

def getUserAns():
    ans = str(input('숫자 입력 : 세자리 숫자 중복 금지'))
    if ans[0] == ans[1] or ans[0] == ans[2] or ans[1] == ans[2] or len(ans) != 3:
        while ans[0] == ans[1] or ans[0] == ans[2] or ans[1] == ans[2] or len(ans) != 3:
            print('중복됨!! / 세자리가 아님!!')
            ans = str(input('숫자 입력 : 세자리 숫자 중복 금지')) 
    list = [ans[0], ans[1], ans[2]]        
    return list

def judge():
    com = getNum()
    while True:
        strike = 0
        ball = 0
        user = getUserAns()
        for i in range(3):
            for j in range(3):
                if i == j and int(user[i]) == com[j]:
                    strike += 1
                elif int(user[i]) == com[j] and i != j:
                    ball += 1
        print("%d 스트라이크" % strike)
        print("%d 볼" % ball)
        if strike == 3:
            print('정답 : ', com)
            print('HomeRun!')
            break
    
    
    
judge()    




















































