# -*- coding:utf-8 -*-

# 조건문 : 흐름 제어

if True: 
    print("와 ~ 조건문") # 들여쓰기는 꼭 해야함 들여쓰기를 안하면 if문인지 일반코드인지 인식 못함
if False:
    print("안나오지")
###############################################################################################
# 우선순위 (산술, 관계, 논리)
# 산술 > 관계 > 논리 
print(10 + 2 > 8 + 3)   # 산술이 관계보다 앞서서 => 12 > 11 => True
print(10 + 2 * 2 > 8 + 3 * 2) # 14 > 14 => False
print(((10 + 2) > 3) and (6 + 4 == 10)) # 13 > 3 and 10 == 10 => True
###############################################################################################
# if 조건A:
    # 코드 
# else:
    # 코드

# 놀이동산 >> A : 성인, 150이상 (값은 입력받아서) 
# 입력시에 => 탑승 가능 or 탑승 불가 출력
height = int(input('키 입력 : '));
age = float(input('나이 입력 : '));
# if height >= 150 and age >= 20:
    # print('탑승 가능')
# else:
    # print('탑승 불가')
    
# if (age >= 20):
    # if (height >= 150):
        # print('탑승 가능')
    # else:
        # print('탑승 불가')
# else:
    # print('탑승 불가')
    
print('탑승 가능'if (age >= 20 and height >= 150) else '탑승 불가')
print((age >= 20 and height >= 150) and '탑승 가능' or '탑승 불가')
#######################################
# 다중 조건문
# Java : if - else if - else
# Python : if - elif - else
# 점수 입력 => 80점 이상은 'A'
#            70점 이상은 'B'
#            60점 이상은 'C'
#            나머지는 'D'를 출력
score = int(input('점수 입력 : '));
if score > 100 or score < 0:
    print('Error')
elif score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')
#######################################
# switch - case : 없음
# in, not in
abc = {"name": "비버", "age" : 19, "phone" : '010-1111-2222'}

print('name' in abc) # key 값이 abd(dict)에 있는지(bool)
print(20 in abc.values())
print('height' not in abc)



















































