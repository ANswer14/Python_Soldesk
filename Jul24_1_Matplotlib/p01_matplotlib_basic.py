# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Numpy : 다차원 배열, 행렬 연산 
#    cmd => pip install numpy

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

# matplotlib에서는 일반적으로 Numpy에 있는 Array를 이용
# Numpy를 사용하지 않더라도, 모든 시퀀스는 내부적으로 Array로 변환을 해서 사용

yData = np.array([12, 31, 1, 2]) # Numpy의 Array를 사용 
xData = [1, 2, 3, 4]            # Numpy를 사용하지 않아도 내부적으로 변환

# 기본 
# plt.plot(yData) # plot : 선 그래프 
# plt.show() # 그래프를 그리겠다

# x, y
# plt.plot(xData, yData)
# plt.show()

# 축
# plt.plot(xData, yData)
# plt.xlabel("x축")        # x축의 이름
# plt.ylabel("y축")        # y축의 이름
# plt.axis([0, 10, 0, 50]) # [xmin, xmax, ymin, ymax]
# plt.show()

# title
# plt.plot(xData, yData)
# f = {"fontsize" : 15, "fontweight" : "light"} # bold, light, ultralight, ...
# plt.title("ㅋㅋ", loc="left") # 제목, 제목위치
# plt.title("ㅎㅎ", loc="center") # 제목, 제목위치
# plt.title("제목", loc="right", fontdict=f) # 제목, 제목위치, 글꼴 fontdict=<dict>
# plt.show()

# style
# plt.plot(xData, yData, "k-.x")
# plt.show()
# 색(c) / 선의 모양(-.) / 마커의 모양
   # 색(c)
   # b : blue / g : green / r : red / y : yellow / k : black
   # w : white / c : cyan
   # plot함수의 color라는 옵션으로 RGB지정하는 것도 가능 !

# 선의 모양(-.)
#    ' : ' : 점선 / ' - ' : 실선 / ' -- ' : dashed line / ' -. ' : 실선 + 점선
#    plot함수의 linestyle이라는 옵션으로 지정하는 것이 가능 !

# 마커의 모양(h)
#    ' . ' : 점 / ' o ' : 동그라미 / ' v ' : 아래 삼각형 / ' ^ ' : 위 삼각형
#    ' < ' , ' > ' : 삼각형 왼쪽, 오른쪽 / ' s ' : 사각형 / ' p ' : 오각형
#    ' h ' : 육각형 / ' * ' : 별 / ' + ' : + 모양 / ' x ' : x 모양
#    plot함수의 marker라는 옵션으로 지정하는 것이 가능 ! 

# grid (격자)
# plt.plot(xData, yData)
# plt.grid(axis="both", color="#997700", linestyle="-.")
# plt.show()

# 눈금
# plt.plot(xData, yData)
# plt.xticks(xData, ["일", "이", "삼", "사"]) # xticks : x축 눈금
# plt.yticks(np.arange(0, 41, 10), ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"])
# plt.tick_params(axis="x", direction="inout", length=5, pad=15,
#            x, y, both    in, out, inout    눈굼의 길이     눈금과 라벨 사이의 거리
                # color="r", labelsize=20, labelcolor="#F15F5F")
#                눈금 색            라벨크기            라벨 색
# plt.show()

# 선 
# plt.plot(xData, yData)

# 실제 y값, xmin, xmax => 지정한 점을 따라서 수평선
# plt.hlines(31, 1, 2, color = "r", linestyles="--")
# 실제 x값, ymin, ymax => 지정한 점을 따라서 수직선
# plt.vlines(1, 31, 12, color="r", linestyles="--")
# plt.show()

# 선 여러개

# yData = np.array([12, 31, 1, 2]) # Numpy의 Array를 사용 
# xData = [1, 2, 3, 4]            # Numpy를 사용하지 않아도 내부적으로 변환
# yData2 = [5, 66, 1, 10]
# plt.plot(xData, yData, "r-")
# plt.plot(xData, yData2, "g:")
# plt.legend(["빨강데이터", "초록데이터"]) # 그래프 순서대로 그래프의 설명
# plt.show()

# 선 여러개 2 (y축을 나눠서)
yData2 = [500, 600, 100, 1000]

x1 = plt.subplot() # 여러 그래프들을 동시에 시각화
p1 = x1.plot(xData, yData, "r-")
x1.set_xlabel("X축")
x1.set_ylabel("Y축")

x2 = x1.twinx() # x축을 공유
p2 = x2.plot(xData, yData2, "g:")
x2.set_ylabel("Y축2")
x1.legend(p1 + p2, ["Red", "Green"])
plt.show()
































