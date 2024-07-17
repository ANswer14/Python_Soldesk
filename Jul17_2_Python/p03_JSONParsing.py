# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from urllib.parse import quote
from json import loads

# 42008a8c8e7402a3fc9d3b1a7df8fee9

# https://api.openweathermap.org/
# data/2.5/weather?q={city name}&appid={API key}

# 도시 이름 : 입력 (영어)
# 요청파라미터 추가 O
# 응답 내용 출력까지

city = quote(input('도시 입력 : '))
print(city)
hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", f"/data/2.5/weather?q={city}&appid=42008a8c8e7402a3fc9d3b1a7df8fee9&units=metric&lang=kr")

res = hc.getresponse()
resBody = res.read()
print(resBody.decode()) # 여기까지가 HTTP 통신

# json__init__
weatherData = loads(resBody) # JS => Python Data
print(weatherData)

# dict : {"key" : "value"}
# list : [1, 2, 3] => 인덱스 값으로    
l = [1, 2, 3]                        # python : list / JS : array
d = {"name" : "홍길동", "age": 30}     # python : dict / JS : object
################################################################
# 날씨 / 기온 / 체감기온 / 습도 / 바람속도
# 데이터를 콘솔창에 츨력
# dict / list 잘 확인하면서 
print(weatherData['weather'][0]['description'])
print(weatherData['main']['temp'])
print(weatherData['main']['feels_like'])
print(weatherData['main']['humidity'])
print(weatherData['wind']['speed'])

































