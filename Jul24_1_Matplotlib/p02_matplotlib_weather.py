# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from xml.etree.ElementTree import fromstring
# 기상청 데이터
#    => 각 시간별 기온(temp)와 습도(reh)를 선 그래프로 표현

# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4141051000
hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=4141051000")

res = hc.getresponse()
res = res.read()
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc("font", family=fontName)
plt.rcParams['axes.unicode_minus'] = False
temp = []
hour = []
reh = []
list = []
count = 0
for w in fromstring(res).iter('data'):
    temp.append(float(w.find('temp').text))
    hour.append(int(w.find('hour').text) + int(w.find('day').text) * 24)
    print(int(w.find('day').text) * 24)
    # hour.append(int(w.find('hour').text))
    reh.append(float(w.find('reh').text))
for i in range(len(hour)):
    count += 1
    list.append(count * 3)
    if hour[i] % 24 == 0:
        count = 0
list.remove(list[0])
list.remove(list[0])
list.remove(list[0])
list.remove(list[0])
list.insert(0, hour[3])
list.insert(0, hour[2])
list.insert(0, hour[1])
list.insert(0, hour[0])
print(hour)
x1 = plt.subplot()
p1 = x1.plot(hour, temp, "r--")
x1.set_xlabel("시간")
x1.set_ylabel("기온")
plt.xticks(hour, list)
x2 = x1.twinx()
p2 = x2.plot(hour, reh, "g:")
x2.set_ylabel("습도")
x1.legend(p1 + p2, ["기온", "습도"])
plt.show()





















































