# =*= coding:utf-8 -*-
import random

# i = random.randint(1, 10) # 1 ~ 10 사이의 정수 중 하나
# print(i)

# 로또번호뽑기 (1 ~ 45 정수 중 6개) => 중복 없이 => 출력

set = {0}
for i,v in enumerate(range(6)):
    ran = random.randint(1, 45)
    print(ran)
    # set = type(set)
    if ran in set:
        while ran in set: 
            ran = random.randint(1, 45)
    set.add(ran)
set.remove(0)
print(set)

num_list = [] # 랜덤으로 뽑은 숫자를 담을 list
count = 0

while count < 6: 
    ran_num = random.randint(1, 45)
    if ran_num not in num_list: # 뽑은 숫자가 list에 안들어있다면 (중복처리)
        num_list.append(ran_num)
        count += 1
for n in num_list:
    print(n, end=' ')