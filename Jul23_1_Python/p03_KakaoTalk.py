# -*- coding:utf-8 -*-

# 카카오톡 내용 정제
# ㅋ : ?, ㅎ : ?, ㅠ : ?, ? : ?, ! : ? => pie차트
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

wc = {"ㅋ":0, "ㅎ":0, "ㅠ":0, "?":0, "!":0}

with open("C:/Users/sdedu/Desktop/file/kakaotalk.txt", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        if " : " in line:
            lines = line.split(" : ", 1) # 첫번째 " : " 에서만 분리
            if len(lines) ==2:
                dialog = lines[-1]
                for w in dialog:
                    if w in wc:
                        wc[w] += 1
print(wc)
                
                
word = []
count= [] # key와 value를 따로 담을 빈 list 생성
for k, v in wc.items():
    word.append(k)
    count.append(v)

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)

c = ['#BBDDCC', '#B2CCCFF', 'FFA7A7', '#E5DDFF', '#DDFFFF']
w = {"width" : 0.7, 'edgecolor': "black", 'linewidth': 5}
plt.pie(count, labels=word, autopct="%.2f%%", wedgeprops=w) # wedgeprops : 테두리
plt.title('카톡 단어 사용량')
plt.show()



















































