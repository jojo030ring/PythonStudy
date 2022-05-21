#### 문자열 ####
'''
    1. 큰 따옴표 작은 따옴표 모두 사용이 가능
    큰 따옴표 3개 연속 사용하여 양쪽을 둘러싸기도 가능
    작은 따옴표 3개 사용 가능
    
    변수에 값을 할당하지 않는다면 주석으로도 사용이 가능하다.
'''

"""Hello world"""
'Python is fun..?'

'''
    안녕하세요
'''


'''
    2. 여러 줄인 문자열을 변수에 대입하고자 할 때 
    1> \n 사용
    2> \'\'\' 또는 \"\"\" 사용

'''


'''
    3. 문자열 연산
    - 문자열 곱하기 
'''

from weakref import WeakKeyDictionary


a='python'
# print(a*2) ## pythonpython

'''
    - 문자열 길이 구하기
'''
a='Life is very short'
# print(len(a)) ## 18


'''
    4. 문자열 인덱싱, 슬라이싱
    - 문자열 인덱싱
'''
a='Life is too short, You need Python.'
# print(a[3]) ## e
# print(a[-1]) ## 음수가 들어가면 뒤에서부터 순회.
# a[0] == a[-0]임. -가 붙으면 그냥 그 숫자가 뒤에서 몇번째인지만 나타낸다 생각하면 됨

''' 
    5. 문자열 슬라이싱
    문자열[시작인덱스 : 끝 인덱스(포함 안됨)]
    시작 <= a < 끝
    [시작:] > 끝 인덱스를 생략하면 그 번호부터 문자열의 끝까지 뽑아낸다.
    [:끝] > 시작 인덱스를 생략하면 시작부터 끝번호까지 뽑아낸다
    
    -도 사용이 가능하다
    [19:-7] == 19번째부터 -8까지 출력함을 의미한다.
'''

# print(a[0:4]) ## Life
# print(a[0:-5]) ## Life is too sort, You need Py

'''
    5. 슬라이싱으로 문자열 나누기
'''

a = '20010331Rainy'
date = a[:8]
weather = a[8:]
# print(date+" : "+weather)

'''
    * 문자열 바꾸기
    Study > Dtudy로 바꾸고 싶다면
    문자열을 배열로 보고 a[0] = D로 재할당 해주면 되는가? ㄴㄴ
    문자열 자료형은 요솟값을 변경할 수 없다.
    >> 슬라이싱을 이용하자.

'''

a = 'Pithon'
b = a[:1] + 'y' + a[2:]
# print(b) ## python

'''
    6. 문자열 포매팅
    정해진 포맷을 정해놓고 변경되는 값만 사삭 대입하는 방법
    현재 온도는 10도 입니다 > 현재 온도는 20도 입니다
    현재 온도는 ~~도 입니다만 정해놓고 ~~에 해당하는 애만 변경하는 것
    - 숫자 바로 대입
    "I ate %d(타겟) apples" % 개수
'''

# a= "I eat %d apples" % 3
# print(a)

'''
    - 문자열 바로 대입
    똑같이 % 뒤에 문자열 적어주면 됨
    그리고 %d가 아니라 문자열이니 %s

'''
a = "I ate %s apples" % "five"
# print(a) ## I ate five apples

'''
    - 숫자 값을 나타내는 변수로 대입
    걍 숫자 넣는 것처럼 "%d" % 변수명


    - 여러 개 넣기
    알맞은 포맷코드 지정해준 다음에 괄호로 묶어서 표현해주면 된다.
    
'''
number = 10
day = "three"
a = "I ate %d apples, so I was sick for %s days" % (number, day)
# print(a) 


'''
    ** 포매팅 연산자와 %를 같은 문자열에 쓸 경우, %를 %%로 나타내야 에러도 안나고 퍼센트도 출력 된다.
    문자열 : %s
    문자 1개 : %c
    정수 : %d
    부동소수 : %f
'''
a="Error is %d%%" % 20
# print(a) #Error is 20%

'''
    7. 포맷 코드 + 숫자 함께 사용
    - 정렬과 공백
'''
a = "%10s" % 'hi'
# print(a) ##          hi(오른쪽 정렬)

a = "%-10sJane" %'hi'
# print(a)  ##hi          Jane(왼쪽 정렬)

'''
    - 소숫점 표현하기
'''
a = "%0.4f" % 3.12341234
# print(a) ##3.1234 > 소숫점 4번째 숫자까지 나타냄

a = "%10.4f" % 2.34314123
# print(a) ##     2.431 / 숫자를 소수점 4번째 자리까지 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하는 예제

'''
    format 함수를 이용한 포매팅
    - 숫자 바로 대입 > 변수도 쌉가능
'''
a = "I ate {0} apples".format(3) ## format함수에 그대로 집어 넣는다.
# print(a) ## I ate 3 apples

'''
    - 문자열 대입 > 변수도 쌉가능
'''
a = "I ate {0} apples".format("three")
# print(a)

'''
    - 2개 이상의 값을 넣기
    {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다.
'''
number = 10
day = "three"
a = "I ate {0} apples. so I was sick for {1} days..".format(number,day)
# print(a) ##I ate 10 apples. so I was sick for three days..

'''
###- 이름으로 넣기
    인덱스를 통해 넣는 것보다 더 편리한 형태라고 한다.
    이런 경우 format 함수에 (name=value)형태의 파라미터가 존재해야 한다.
    

'''
a= "I ate {number} apples. so I was sick for {day} days....".format(number=10, day="fifty")
# print(a)

'''
### 인덱스와 이름을 혼용해서 넣을 수도 있다.

'''
a = "I ate {0} apples, so I was sick for {day} days".format(10, day="five")
# print(a)

'''
    - 왼쪽, 오른쪽 정렬
    :<10 >> 치환되는 문자열을 왼쪽으로 정렬하고, 문자열의 총 자릿수를 10으로 맞춤
    :>10 >> 치환되는 문자열을 오른쪽으로 정렬, 문자열의 총 자릿수를 10으로 맞춤
'''
# print("{0:>10}".format("hi")) ##         hi


'''
    - 가운데 정렬 :^

'''
# print("{0:^10}".format("hi")) #    hi    

'''
    - 공백 채우기
    정렬할 때 공백문자 대신 지정한 문자 값으로 채워넣는 경우
    이 때 대신 채워넣을 문자는 <, >, ^바로 앞에 넣어야 한다.
'''
# print("{0:=^10}".format("hi")) ##====hi====
# print("{0:!<10}".format("hi")) ##hi!!!!!!!!
############## 문자열 관련 함수들 전까지만 힘내자!!!! #############
y = 3.423455667
# print("{0:10.4f}".format(y)); #     3.4235

'''
    - { 또는 } 문자 표현하기
    {{ }}
'''

'''
    8. f문자열 포맷팅
    3.6버전부터는 f문자열 포매팅 기능을 사용가능
'''

name='hong gil dong'
age=30
# print(f'My name is ... {name}. Age : {age}')


d={'name' : '홍길동', 'age' : 30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]} 입니다.')
# 나의 이름은 홍길동입니다. 나이는 30 입니다.

'''
    딕셔너리 > f문자열 포매팅에서 다음과 같이 사용할 수 있음.
    딕셔너리는 key와 value라는 것을 한쌍으로 갖는 자료형이다.
'''

'''
    정렬은 다음과 같이 할 수 있음.
'''
# print(f'{"h1":<10}') # 왼쪽 정렬
# print(f'{"h1":>10}') # 오른쪽 정렬
# print(f'{"h1":^10}') # 가운데 정렬
'''
h1        
        h1
    h1  
'''

'''
    공백 채우기는 다음과 같이 할 수 있음.
'''
# print(f'{"h1":=^10}')
# print(f'{"h1":!<10}')
'''
====h1====
h1!!!!!!!!
'''

'''
f문자열에서 {{ }} 문자를 표시하려면 다음과 같이 두 개를 동시에 
사용해야 한다. 
'''



'''
    8. 문자열 관련 함수
    문자열 관련 함수는 내장함수임.
    내장함수를 사용하려면 문자열 변수 이름 뒤 .을 붙인 다음 함수 이름을 사용하면 됨    

'''

# count : 문자 개수 세기
a = 'hobby';
# print(a.count('b')) # 문자열 a 에서 b가 몇 번이나 들어가는지 알려줌. ## 2

# find : 위치 알려주기
# 문자가 처음 나온 위치 반환. 문자가 존재하지 않으면 -1을 반환
# 파이썬은 숫자를 0부터 센다.

a = 'Life is too short, so You need a python...'
# print(a.find('p')) ## 33

# index : 위치 알려주기
# 문자가 처음 나온 위치를 반환. 문자가 존재하지 않으면 오류 발생

# print(a.index('L')) ## 0


# <문자열 삽입> : join
# print(",".join('abcd')) ## a,b,c,d
'''
    삽입할 문자.join(삽입당할 문자열)
'''

# print("!".join(['a','b','c','d'])) ## a!b!c!d
'''
    리스트나 튜플도 입력으로 사용이 가능하다.
    다만 요소들이 int형이면 안된다는 단점..
    
'''

# 소문자 -> 대문자 : upper()
# 대문자 -> 소문자 : lower()
# 왼쪽 공백 삭제 : lstrip()
# 오른쪽 공백 삭제 : rstrip()
# 양쪽 공백 삭제 : strip()
a = 'hi'
# print(a.upper())
a = 'HI'
# print(a.lower())

a='  hi  '
# print(a.lstrip()) ## hi
# print(a.rstrip()) ##   hi
# print(a.strip())  ## hi

# 문자열 바꾸기 : replace
a = 'Life is too short. you need to learn java..'
# a.replace('java','python') ## 원본을 바꾸는 함수는 아님
# print(a.replace('java','python')) ## Life is too short. you need to learn python..

# 문자열 나누기 : split
a='Life is too short, you need to learn python.'
# print(a.split()) ## ['Life', 'is', 'too', 'short,', 'you', 'need', 'to', 'learn', 'python.']
                   ## 리스트 형태로 리턴된다.

b = "a:b:c:d"
# print(b.split(':')) ## a,b,c,d가 들어간다.
'''
    파라미터로 특정 값이 들어가는 경우 그 값을 기준으로 나눠주지만.
    파라미터를 주지 않으면 스페이스, 텝, 엔터 등으로 문자열을 나눈다.
'''



