# -*- coding:utf-8 -*-

# function(함수)
# def 함수명(파라미터명):
    # code
def test():
    print("잠못잔 사람")
    
def test2():    # ':'을 썼으면 그 다음줄에는 반드시 들여쓰기를 해야!!
    pass            # : 뒤에 코드 적을것이 없을 때, 자리채워주라는 의미 

# 정수 2개를 넣으면 그 합을'출력'하는 함수
def printSum(a=5, b=8): # 호출할 때 값을 안넣어주면 함수파라미터의 값을 
                        # 기본값으로 사용
    print(int(a) + int(b))
    
# 정수 3개를 넣으면 그 합을 '출력'하는 함수
def printSum2(a=1, b=2, c=3):   # overloading이 안됨 => 모든 함수명이 다 달라야...
    print(a + b + c)

# 정수 2개를 넣으면 그 합을 '구하는' 함수
def getSum(a, b):
    return a + b

# 정수 2개를 넣으면 사칙연산 결과를 '구하는' 함수
def getEnumerate(a, b):
    '''
        설명서...
        이 설명서는 ~~~~~~~~~~~
    '''
    sum = a + b
    minus = a - b
    mul = a * b
    divide = a / b
    return sum, minus, mul, divide
 
#############################################
help(getEnumerate)
help(print)
test()
printSum(1, 4)
printSum()
printSum2(4, 5, 6)
printSum2()
print(getSum(1, 2))
print(getEnumerate(1, 2))
# a, b, c, d = getEnumerate(1, 2)
# print(a)

a, b, _, d = getEnumerate(1, 2) # _ 처리하면 곱하기 결과 안 가져올 수 있음
print(a, b, d)