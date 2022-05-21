# animal = '이불'
# name = '쭈꾸'
# age = 7
# hobby = '사랑한다말하기'
# is_adult = (age >= 10)
# print ('우리집 '+animal+'의 이름은 '+name+'예요')
# print(name+'는 '+str(age)+'살이고, '+hobby+'를 아주 좋아해요.')
# print(name+'는 어른일까요? '+str(is_adult))

# # quiz

# station = "사당"
# print(station+"행 열차가 들어오고 있습니다.")
# station ="신도림"
# print(station+"행 열차가 들어오고 있습니다.")
# station ="인청공항"
# print(station+"행 열차가 들어오고 있습니다.")


# # 연산자
# print(not(1!=3))
# # and 연산자 : and 또는 &
# # or 연산자 : or 또는 |
# print(5>4>3) #true
# print(5>4>7) #false

# from random import *
# print(int(random() * 10)+1) ## 1 ~ 10

# print(int(random() * 45)+1) ## 1부터 45이하의 임의의 값 생성

# '''
# 이걸 편하게 하기 위해...
# randrange() 라는 메서드 존재하고 사용할 수 있음
# 정수값을 리턴. 마지막 값은 포함 X
# '''
# print(randrange(1,46))

# '''
#     randint(start, final)
#     start, final 모두 포함
# '''
# print(randint(1,45))

# #quiz 2
# day = randint(4,28)
# print('오프라인 스터디 모임 날짜는 매월'+str(day)+'일로 선정되었습니다.')


# sentence = '나는 소년입니다'
# print(sentence)
# sentence = """
#     나는 소년이에요.
#     파이썬 최고~
# """

# print(sentence)

'''
    슬라이싱
'''
jumin = "991020-1234567"
print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])
print("월: "+jumin[2:4])
print("일 : "+jumin[4:6])

print("생년월일 : "+jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : "+jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에서부터) : "+jumin[-7:])
'''
    뒤에서 추출하든 아니든 진행 방향은 항상 왼쪽에서 오른쪽임을 생각하자.

'''


'''
    문자열 처리 함수
'''
python = "Python is amazing"
print(python.lower()) # 소문자로 바꿔주는 함수
print(python.upper()) # 대문자로 바꿔주는 함수
print(python[0].isupper()) # 해당 문자가 대문자인지 조회하는 함수
print(len(python)) # 문자열의 길이를 구하는 함수
print(python.replace('Python', 'Java')) # python에서 Python이라는 글자를 찾아서 java로 변경

index = python.index('n')
print(index)
index = python.index('n', index+1)
'''
    index함수의 매개변수
    - index('문자') > 문자가 위치하는 곳
    - index('문자', 시작위치) > 시작위치부터 찾음.
    index+1이라고 지정하면 첫 번째 n이 나온 곳 바로 다음부터가 검색범위에 들어가는 것이다.
    
    비슷한 메서드 : find('문자')
    
    차이 : 원하는 값이 없으면 find는 -1 / index는 에러 뜸
    
'''
print(python.count('n')) # n이라는 문자가 몇 번 등장했는지?


'''
########################################################################
                        문자열 포맷팅
########################################################################

'''
# 방법 1
print("나는 %d살 입니다" % 20) # %d 로 지정해주었으므로 정수만 가능하다.
print("나는 %s을 좋아합니다." % 'python') # %s는 문자열
print("Apple은 %c로 시작해요." %'A')

## 사실 %s로 다 받을 수 있다.

## 두 가지 이상의 값을 받을 때
print("나는 %s색과 %s색을 좋아합니다." % ("파란","빨간"))


# 방법 2
print("나는 {} 살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("파란","빨간"))
## 바로 위 문장은 다음과 같다.
print("나는 {0}색과 {1}색을 좋아합니다.".format("파란","빨간"))
## 0과 1을 바꾸는 것만으로 순서를 바꿀 수 있다.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아합니다.".format(age=20, color ="붉은"))

# 방법 4
# 파이썬 3.6 이상부터 가능
age = 20
color = "붉은"
print(f"나는 {age}살이며, {color}색을 좋아합니다.")
# 변수의 문자를 적용할 수 있게 됨


'''
########################################################################
                            탈출 문자
########################################################################

'''
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# 걍 이스케이프 문자 쓰는거 강의하시는듯
# \\ == \
# \" \' == "  '
# \r == 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple
# 커서를 맨 앞으로 이동해서
# Red공백1칸만큼 지우고 Pine을 써서 저렇게 나옴
# \b  = 백스페이스
'''
########################################################################
                               퀴 즈
########################################################################

'''
url = 'http://naver.com'
frontindex = url.index('/') +2
backindex = url.index('.')
#print(input[frontindex:backindex])
input = url[frontindex:backindex]
password = input[:3]+str(len(input))+str(input.count('e'))+'!'
print("{0}의 비밀번호는 {1}입니다.".format(url, password))


'''
    url = "http://naver.com"
    my_str = url.replace("http://","") # 규칙 1
    my_str = my_str[:my_str.index('.')] # 규칙 2
    password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+'!'
    print(password)
'''
