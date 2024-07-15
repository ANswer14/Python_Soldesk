# -*- coding:utf-8 -*-

# for (int i = 0; ... )        : X
# for (int ii : i)             : O (Java의 for-each문에 해당하는 반복문)

l = [123, 45, 6, 78, 910]
for ll in l:        # for (int ll : l)
    print(ll)
print()
    
# ㅋ을 10번 출력
for z in range(10):
    # print(z)
    print("ㅋ")
print()
# 1 ~ 20 까지의 정수 중에서 홀수만 출력
for z in range(1, 21, 2):
    print(z)
print()
###################################################################
# while문 : O
while True:
    y = int(input("y : "))
    if y % 2 == 0:
        print('짝수')
        break
# do{}while문 : X
###################################################################
# enumerate : 반복문을 사용할 때 몇 번 반복되었는지 확인이 필요할 때 사용
#            (인덱스, 값) 형태의 tuple로 리턴
ll = ['컴퓨터', '모니터', '키보드', '마우스']

for i, v in enumerate(ll):
    print(i + 1, v)
print("-----------------------")        

score = [10, 54, 54, 3, 234, 6, 12, 345, 7, 6 ,456]
# 1등 학생은 몇번째에 ? / 점수는 몇점인지? 출력
maxS = 0
maxI = 0
for i, v in enumerate(score):
    if v > maxS:
        maxI = i
        maxS = v
print(maxS)
print(score.index(54))

print(maxI)

for i, v in enumerate(range(10)):
    print("index", i)
    print("value", v)

















































