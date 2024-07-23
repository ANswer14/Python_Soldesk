# -*- coding:utf-8 -*-

sss = ["ㅋㅋㅋ", "ㅁㅁㅁ", "ㅂㅂㅂ", "ㅎㅎㅎ", "ㅁㅁㅋㅋㅋ", "ㄹㄹㄹ"]
for s in sss:
    # 찾는 문자열이 존재하는 경우 : 그 문자열이 있는 인덱스값을 리턴
    # 찾는 문자열이 존재하지 않는 경우 : -1 리턴
    print(s.find("ㅋㅋㅋ"))
    print(s.find("ㅊㅊㅊ"))
    print("-------------")
# 조조(맹덕), 유비(현덕), 손권(중모)
# 책을 훑어보면서... => 위의 인물들이 몇 번 언급됐는지 카운팅하기!
# 인물, 언급힛수의 형태로 => csv파일에 저장
# count = 0;
# ansCount = 0;
# countJ = 0;
# countY = 0;
# countS = 0;
# for i in range(10):
    # count += 1;
    # if i != 9:  
        # f = open(f"C:/Users/sdedu/Desktop/file/ThreeKingdoms/ThreeKingdoms/ThreeKingdoms0{count}.txt", "r", encoding="UTF-8")
    # elif i == 9:
        # f = open(f"C:/Users/sdedu/Desktop/file/ThreeKingdoms/ThreeKingdoms/ThreeKingdoms10.txt", "r", encoding="UTF-8")
    # abc = list(f.read().split(" "))
    # # data = f.read()
    # for data in abc:
        # if data.find("조조") > -1 or data.find('맹덕') > -1:
            # countJ += 1
        # if data.find("유비") > -1 or data.find('현덕') > -1:
            # countY += 1
        # if data.find("손권") > -1 or data.find('중모') > -1:
            # countS += 1
        # elif data.find("손권") > -1 and data.find('중모') > -1:
            # countS += 2
    # # countJ += data.count('조조') + data.count('맹덕')
    # # countY += data.count('유비') + data.count('현덕')
    # # countS += data.count('손권') + data.count('증모')
# f = open("C:/Users/sdedu/Desktop/file/fil6.csv", "w", encoding="UTF-8")
# f.write('조조, ' + str(countJ) + "\r\n")
# f.write('유비, ' + str(countY) + "\r\n")
# f.write('손권, ' + str(countS) + "\r\n")
        #
# f.close()


wc = {"조조" : 0, "유비" : 0, "손권" : 0}

for i in range(1, 11):
    fileName = "C:/Users/sdedu/Desktop/file/ThreeKingdoms/ThreeKingdoms/ThreeKingdoms%02d.txt" % i
    
    with open(fileName, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.split(" ")
            for word in line:
                # print(word)
                if word.find("조조") != -1 or word.find("맹덕") != -1:
                    wc["조조"] += 1
                elif word.find("유비") != -1 or word.find("현덕") != -1:
                    wc["유비"] += 1
                elif word.find("손권") != -1 or word.find("중모") != -1:
                    wc["손권"] += 1
for key in wc:
    print(key)
for val in wc.values():
    print(val)
with open("C:/Users/sdedu/Desktop/file/fil6.csv", "w", encoding="UTF-8") as f:
    for k, v in wc.items():
        f.write(f"{k},{v}\n")
        
print("END 1!")
     















































