
#1. 윤년 구하기
year = int(input("연도를 입력하세요"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)

#2. 출력하기 for문 사용
num = int(input("숫자를 입력하시오"))
for number in range(num,0,-1):
    print(number)


