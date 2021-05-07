str = "멋쟁이 사자처럼"
str2 = "은 좋은 동아리입니다"

print(str + str2)
print(str * 3)
print(str[0])

#슬라이싱
print(str[0:4])

#문자열 길이
print(len(str))

#특정 문자 등장 횟수
print(str.count("사"))

#특정 문자 기준으로 나누기
print(str.split(" "))
print(str.split()) 

#특정 문자 인덱스 찾기 : FIND, INDEX
print(str.find("사")) 
print(str.index("사"))

#리스트 (내장함수)
li = [3,1,"배가", 4, "고파요",5,1]
li2 = [3,1, 4,5,1]


#인덱싱 슬라이싱
print(li[0:3])

#리스트 길이
print(len(li))

#리스트 원소 오름차순 정렬: sort()
#printf(li.sort()) 안됨, 반환 x
li2.sort()
print(li2)

#특정 원소 인덱스 반환
print(li.index("배가"))

#특정 원소의 등장 횟수
print(li.count("고파요"))


#딕셔너리 (내장함수)
pairs = {"잔나비" : "뜨거운" , "소히": "산책", "홍크": "어쩌면"}

#하나의 ket, value 추가
pairs["스탠딩 에그"] = "휴식"
print(pairs)

#key, value 한쌍 삭제
del pairs["잔나비"]
print(pairs)

#key로 value를 얻기
v = pairs.get("소히")
print(v)

#제어문 - 분기문

score = int(input("정수를 입력하시오"))
if(score >= 85):
    print("pass")
else:
    print("fail")

activity = input("너 동아리 뭐해? :")
if(activity == "멋사"):
    print("오")
else:
    printf("응")

money = int(input("돈 얼마 있어?"))
if (money >= 5000):
    print("아웃백 가자")
else:
    if(money >= 3000):
        print("학식 먹자")
    else:
        if(money >= 1000):
            print("컵라면 먹자")
        else:
            print("공기밥 먹자")

#elif문
if (money >= 5000):
    print("아웃백 가자")
elif (money >= 3000):
    print("학식 먹자")
elif (money >= 1000):
    print("컵라면 먹자")
else:
    print("공기밥 먹자")

#반복문
for score in range(10):
    print(score)





   
