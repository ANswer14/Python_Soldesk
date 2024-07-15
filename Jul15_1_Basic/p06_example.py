# -*- coding:utf-8 -*-
import random
from random import randint
import time

# Java (null) = Python (None)

# 가위바위보 (함수)=> 한번 질 때까지 => 총 몇번 이겼는지 출력

# def getComAns():
    # ans = random.randint(1,3)
    # return ans
    #
# def getUserAns():
    # ans = str(input('유저의 답(가위/바위/보)'))
    # if ans not in ('가위', '바위', '보'):
        # while ans not in ('가위', '바위', '보'):
            # ans = str(input('유저의 답(가위/바위/보)'))
        # if ans =='가위':
            # ans = 1
        # elif ans == '바위':
            # ans = 2
        # elif ans == '보':
            # ans = 3
    # elif ans in ('가위', '바위', '보'):
        # if ans =='가위':
            # ans = 1
        # elif ans == '바위':
            # ans = 2
        # elif ans == '보':
            # ans = 3
    # return ans
    #
# def goJudge():
    # draw = 0
    # win = 0
    # while True:
        # com = getComAns()
        # user = getUserAns()
        # if com == 1:
            # comA = '가위'
        # elif com == 2:
            # comA = '바위'
        # elif com == 3:
            # comA = '보'
        # if com - user == 1 or com - user == -2:
            # print('컴퓨터의 답 : ', comA, '패배!')
            # break
        # elif com - user == 0:
            # print('컴퓨터의 답 : ', comA, '무승부!')
            # draw += 1
        # elif com - user == -1 or com - user == 2:
            # print('컴퓨터의 답 : ', comA, '승리!')
            # win += 1
            #
    # return win, draw
    #
# def printResult(win, draw):
    # print('승리 : ', win, '무승부 : ', draw)
    #
# def start():
    # win, draw = goJudge()
    # printResult(win, draw)
    #
# start()    

handTable = [None, '가위', '바위', '보']

def printRule():
    print("--------")
    for i,h in enumerate(handTable):
        if i != 0:
            print("[%d] %s" % (i, h))
    print("--------")
    
def comFire():
    return randint(1, 3)
    
def userFire():
    print("--------")
    uh = int(input('뭐 낼 까 ? :'))
    print("--------")
    if (1 <= uh <= 3):
        return uh
    else:
        print("잘못입력")
        return userFire()
        
def printHand(uhuh, chch):
    print('유저 : %s' % handTable[uhuh])
    print('컴퓨터 : %s' % handTable[chch])
    
def judge(uhuh, chch):
    t = uhuh - chch
    if t == 0:
        print('무승부')
        return 0
    elif t == -1 or t == -2:
        print('패배')
        return 999
    else:
        print('승리')
        return 1
        
def playGame():
    printRule()
    win = 0
    while True:
        uHand = userFire()
        cHand = comFire()
        printHand(uHand, cHand)
        result = judge(uHand, cHand)
        if result == 999:
            print("-=-=-=-=-=-=-=-=")
            print("종료 !")
            
            if win >= 10:
                time.sleep(1) # Java의 Thread.sleep()
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print('개고수')
            elif win >= 5:
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print('좀 치네 ?')
            else:
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print(".", end="")
                time.sleep(1)
                print('삭제해라')
            
            break
        win += result
    print('%d승으로 종료 !' % win)
#################################################3
playGame()
        

































