4# -*- coding:utf-8 -*-
import random

# UP/DOWN 게임 (함수)
# 유저의 이름을 입력받고 환영하는 인사를 출력
# (컴퓨터) 1 ~ 100사이의 랜덤한 숫자를 하나 뽑아서
# 유저에게 정답을 입력하게 했을 때
# 저 범위의 숫자가 아니면 다시 입력하도록
# 입력한 숫자가 정답보다 작으면 'UP', 크면 'DOWN' 출력
# 정답을 맞췄을 때는 몇 번만에 맞췄는지 출력 + 종료
# 정답 기회는 총 10번 

def getName():
    name = input('유저 이름 : ')
    return name

def getNum():
    ran = random.randint(1, 100)
    return ran

def getAns():
    ans = int(input('정답 입력 : '))
    if ans < 1 or ans > 100:
        while ans < 1 or ans > 100:
            ans = int(input('정답 입력 : '))
    return ans

def play():
    print(getName(), '님 환영합니다')
    ran = getNum()
    for i,v in enumerate(range(10)):
        ans = getAns()
        if ans < ran:
            print('UP!')
        elif ans > ran:
            print('DOWN!')
        else:
            print('정답!', i + 1, '번만에 맞춤!')
            print('정답운', ran, '!')
            break
        if i == 9:
            print('10번의 기회 소진!')
play()
















































