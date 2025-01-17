# -*- coding:utf-8 -*-

# str
s = "Can't tuna kkk"
print(s)
print(s[0])
print(s[0:6])   # (0번째부터 (6-1)번째까지의 문자열
print(s[2:10:2])# (2번째부터 (10-1)번째까지의 문자열을 2칸씩 건너서 출력)
print(s.count('k'))
print("-----------------------------------------------")

# List : 리스트 (순서 O, 중복 O, 수정 O, 삭제 O)
a = [123, 4, 56, 789, 1011]
print(a, type(a))
print(a[0]) # a의 인덱스0의 요소
print(a[0:3]) # a의 인덱스0 ~ 3번째까지의 요소 => 총 3개의 요소
print(a[1:3])
print(a[0:5:2]) # a의 인데스0 ~ 5까지의 요소 중 2개씩 건너뚜ㅟ어서
print(a[-1]) # a의 뒤에서 첫번째 요소

print(len(a))   # 요소의 갯수
a.append(1213)  # 끝에 요소 추가
a.insert(2, 1415) # 중간에 요소 추가(인덱스 2에 추가)
a[4] = 7788     # 수정(인덱스 4의 요소를 7788로)
del a[0]        # 삭제(인덱스 0의 요소 삭제)

# a.sort()        # 오름차순 정렬
a.sort(reverse = True) # 내림차순 정렬
print(a)
print("-----------------------------------------------")

# Tuple : 순서 O, 중복 O, 수정 X, 삭제 X
# tuple1 = ('1', '2', '3')
# del tuple1[0] 삭제 X
# tuple1[0] = 'c' 수정 X
# print(tuple1)

t = (1, 2, 3, 4, 5, 4, 4)
print(t)
print(t.index(5))   # index 해당 위치에 있는 값을 반환
print(t.count(4))   # 이 요소가 튜플안에서 몇개가 있는지 그 갯수를 반환

# a1 = 20
# b1 = 1
(a1, b1) = (10, 20) # 값을 줄 때 튜플로 묶어서 O / 소괄호 없어도 됨
print(a1)
print(b1)
(a1, b1) = (b1, a1) # 값 바꾸기
print(a1)
print(b1)
x, y, z = 10, 20, 30
x, y, z = z, x, y
print(x, y, z)
print("------------------------------------------------")
# Set(집합) : 중복 제거, 순서는 랜덤
s = {"ㅋ", "ㅋ", "ㄹ","ㅃ","ㅃ"}
print(len(s))
s = list(s)
print(s)
print("------------------------------------------------")
# Dict (= map)
d = {"name": "곽두팔", "age": 12}
print(type(d))
print(d["name"])
print(d["age"])
print(d)
print("------------------------------------------------")
# Range
r = range(10)           # 0 ~ (10-1)까지의 정수 범위 
print(r, type(r))

r2 = range(2, 10)       # 2 ~ (10-1)까지의 범위
r3 = range(2, 10, 3)    # 2 ~ (10-1)까지의 범위를 3씩 건너서
print(r2, r3)

# 0 ~ 9 까지 있는 list 출력
print(list(range(10)))

# 1 ~ 20 중 홀수만 있는 list 출력
print(list(range(1, 21, 2)))

a = [range(1, 21, 2)]
print(type(a[0]))