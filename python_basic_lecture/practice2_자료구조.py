'''
########################################################################
                            리 스 트
########################################################################

'''
number = [10,20,30]
#print(number)
# 10이 몇 번째에 있는가?
#print("10의 위치는 {0}입니다.".format(number.index(10)))
# 33추가
number.append(33)
#print(number)

# 10과 20사이 15삽입
number.insert(1,15)
#print(number)

# 뒤에서 부터 뺌
# print("맨 뒤의 원소 %d 을/를 뺐습니다." % number.pop())
# print(number)
# print("맨 뒤의 원소 %d 을/를 뺐습니다." % number.pop())
# print(number)
# print("맨 뒤의 원소 %d 을/를 뺐습니다." % number.pop())
# print(number)

# 원소의 수 세기
number.append(10)
# print(number)
# print("10의 개수는 %d개 입니다." % number.count(10))

# 정렬
num_list = [5,4,2,6,7,1]
num_list.sort()
# print(num_list)

# 순서 뒤집기 >> 역순정렬 하고싶다면 정렬을 먼저 하고 순서뒤집기를 해야한다.
# 아니면 그냥 1,7,6,2,4,5의 형태로 출력된다.
num_list.reverse()
# print(num_list)

#모두 지우기
num_list.clear()
# print(num_list)

#다양한 자료형을 함께 사용 가능
mix_list = ["string",10,[True,False]]
# print(mix_list)

# 리스트의 확장
num_list.extend(mix_list)
# print(num_list)

'''
########################################################################
                                사    전
########################################################################

'''
cabinet = {3 : 'mina', 100 : 'jumi', }
# 사전의 출력
# print(cabinet)
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))

# 주의 !
'''
    - cabinet[key]
    없는 키를 참조하면 에러를 뱉는다.
    - cabinet.get(key)
    none을 뱉고 프로그램을 정상 실행시킨다.
    - cabinet.get(key,"default value")
    key값이 없으면 value라고 대신 표현한다
    데이터가 삽입되진 않는다.
'''

#print(cabinet.get(5,"없는 인덱스 입니다."))
#print(cabinet)

# key값의 확인
# print(3 in cabinet)
# print(5 in cabinet)

'''
    key값은 string이 될 수도 있다.
'''
# 값의 삽입
# print(cabinet)
# cabinet["A-3"] = "hyunju"
# cabinet["C-20"]="minhoo"
# print(cabinet)

# 값의 삭제
# del cabinet["A-3"]
# print(cabinet)

# key 들만 출력
# print(cabinet.keys())

# value 들만 출력
# print(cabinet.values())

# key, value 쌍으로 출력
# print(cabinet.items())

# 쌍 모두 비우기
# cabinet.clear()
# print(cabinet)


'''
########################################################################
                                튜    플
########################################################################

'''

menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# 추가, 삭제 불가능

# 한 번에 대입하기
name, age, hobby = ("jongho",20,"coding")
# print(name, age, hobby)

'''
########################################################################
                                세    트
########################################################################

'''
# 집합 : 중복이 안되고 순서가 없음

my_set = {1,2,3,3,3}
# print(my_set)

java={"minju","hoyoung","yeji"}
python=set(["yeji","hoyoung"])

# 교집합 : 자바와 파이썬 모두 할 수 있는 사람
# print(java & python)
# print(java.intersection(python))

# 합집합 : java도 할 수 있거나 python도 할 수 있는 개발자
# print(java | python)
# print(java.union(python))

# 차집합 : java만 할 줄 아는사람
# print(java - python)
# print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
# python.add('taewon')
# print(python)

# java를 잊었어요.
# java.remove("hoyoung")
# print(java)

'''
########################################################################
                            자료구조의 변경
########################################################################

'''
# menu = {"커피","우유","주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)


'''
########################################################################
                            자료구조의 변경
########################################################################

'''
from random import *
list =[]
for i in range(0,20) :
    list.append(i+1)
shuffle(list)
first_prize = sample(list,1)[0]
print(first_prize)
list.remove(first_prize)

second_prize = []
for i in range(2,5) :
    second_prize.append(i)        

print("-- 당첨자 발표--\n치킨 당첨자 : {0}\n커피 당첨자 : {1}\n-- 축하합니다. --".format(first_prize,second_prize))
