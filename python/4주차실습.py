#중첩된 리스트 만들기
li = [1,2,3,['a','b','c']]
print(li)

#중첩된 리스트 요소에 접근하기
print(li[3])
print(li[3][1])

#리스트 길이 구하기
print(len(li))

#리스트 요소 추가하기
li.append(4)
print(li)

#리스트 요소 삽입하기
li.insert(0,5)
print(li)

#리스트 요소 제거하기
del li[3]
print(li)

#딕셔너리 만들기
dic = {1:"하나", 2:"둘", 3:"셋"}
print(dic)

#딕셔너리 추가하기
dic[4] = "넷"
print(dic)

#딕셔너리 삭제하기
del dic[4]
print(dic)
