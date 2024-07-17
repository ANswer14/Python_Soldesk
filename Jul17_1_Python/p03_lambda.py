# -*- coding:utf-8 -*-

# 람다(lambda)함수
#    장점 : 메모리 절약, 가독성 향상, 코드가 간결
#        일반 함수 : 함수 생성 => 메모리에 할당
#        람다 함수 : 즉시 실행함수 => 메모리 초기화
#    표현법 : 
#        lambda 파라미터 : 표현식

# 변수를 할당하는 일반적인 함수
def hab(num):
    x = num + 100
    return x
print(hab(100))

# 람다함수
(lambda num: print(num + 100))(100)

# 숫자 두개 넣으면 그 곱을 출력 하는 함수
(lambda num1, num2: print(num1 * num2))(10, 20)

# 숫자 두개 넣으면 그 합을 구하는 함수
hab2 = (lambda num3, num4: (num3 + num4))(1, 3) # return 안써도 return이 자동으로 됨
print(hab2)
























































