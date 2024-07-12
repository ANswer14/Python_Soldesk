# -*- coding:utf-8 -*-

# 정수 2개를 입력 받아서, 사칙연산에 대한 결과와
# 앞의 수를 뒤의 수로 나눴을 때의 나머지 값을 출력

num1 = int(input('정수 1 : '))
num2 = int(input('정수 2 :'))
plus = num1 + num2
minus = num1 - num2
mul = num1 * num2
divide = num1 / num2
print(plus, minus, mul, divide)
rest = num1 - (int((num1 / num2)) * num2) # == num1 % num2
print(rest)
###########################################################
f = num1 // num2    # 몫
print(f)


g = num1 ** num2    # 거듭제곱
print(g)

z = 'ㅋㅋㅋ'
# h = num1 + z
h = str(num1) + z   # 문자열 결합
print(h)

i = num1 * z        # 숫자 * 문자열 => 문자열 반복
print(i)
###########################################################
# x = x + 3
num1 += 3
print(num1)

# ++, --는 없음
# num1++
# print(num1)
###########################################################
###########################################################
j = num1 > 10
print(j)

# && : and , || : or  
k = (num1 > 10) and (num2 < 3)
print(k)

# ! : not
l = not k 
print(l)

# m : x가 5이상 ~ 10이하 : True / 아니면 False 담아서 출력
# m = (num1 >= 5 and num1 <= 10)
m = (5 <= num1 <= 10)
print(m)
###########################################################
# 3항연산자
# Python에는 있다고 하는 사람도 있고, 없다고 하는 사람도 있음...
# [참일때의 값] if [조건식] ekse [거짓일때의 값]
# 정수를 하나 입력받아서 => 그게 짝수면 '짝수', 홀수면 '홀수' 출력

n = int(input('n : '))
ans = '짝수' if n % 2 == 0 else '홀수'
print(ans)

# 위의 버전이 너무 가독성이 안좋아서 python 3.8버전 이후로...
# [조건식] and [참일때의 값] or [거짓일때의 값]
print(n % 2 == 0 and "짝수" or "홀수")






















