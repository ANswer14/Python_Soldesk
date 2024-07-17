# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

# fb780098b6771f02c4682abea4d1d8cf

# https://dapi.kakao.com/v3/search/book

# 책 이름 검색해서 책 제목 - 작가 / 할인가 / 도서 소개 출력

hc = HTTPSConnection("dapi.kakao.com")
book = quote(input('책 이름 : '))
dict = {"Authorization": "KakaoAK fb780098b6771f02c4682abea4d1d8cf"}
hc.request("GET", f"/v3/search/book?query={book}", headers=dict)
res = hc.getresponse()
resBody = res.read()
print(resBody.decode())

bookData = loads(resBody)
books = bookData['documents'] 
# print(bookData["documents"][0]["title"], end=" - ")
# print(bookData["documents"][0]["authors"][0])
# print(bookData["documents"][0]["sale_price"])
# print(bookData["documents"][0]["contents"])
for b in books:
    try:
        print(b["title"], "-", b["authors"][0])
        # print(b["title"], "-", ", ".join(b["authors"]))
                                # .join() : list를 문자열로
                                # 구분자.join() : list의 요소들을 구분자로 나눠 
                                #             하나의 문자열로 합쳐줌
                                # ex( ", ".join(['a', 'b', 'c']) => a, b, c
        print(b["sale_price"])
        print(b["contents"])
    except Exception as e:
        print('---------------')
# for i, v in enumerate(bookData["documents"]):
    # try:
        # for j, c in enumerate(bookData["documents"][i]['authors']):
            # print(bookData["documents"][i]["authors"][j], end=" ")
        # print()
        # print('---------------')
    # except Exception as e:
        # print("", end="")





















