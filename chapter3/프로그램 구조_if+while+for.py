'''
    <조건/제어문 : if>
    1. if문
    - 구조
        if 조건식 : 
            실행문
        else : 
            실행문
    - 들여쓰기
        바로 아래 문장부터 if문에 속하는 모든 문장에 
        들여쓰기(indentation)를 해주어야 한다. 
        중괄호가 없는 대신 들여쓰기로 범위를 판단한다. 주의하자.
    - 조건문 다음 콜론을 잊지 말자.
    
'''
from click import prompt


money = 10000
if(money >= 39999) :
    print("택시 쌉가능")
else : 
    print("미친놈아 버스나 타라") ## 만원 밖에 없기 때문에 버스나 타야함
    
'''
    - and, or, not
    조건을 판단하기 위한 연산자.
    x or y : x나 y 중 하나만 참이어도 참
    x and y : 둘 다 참이어야 참
    not x : 거짓이면 참

'''
money = 2000
card = True
if money >= 3000 or card :
    print("택시를 타고가는 게 좋겠군..")
else :
    print("어딜 감히 택시를 타느냐 걸어가거라")
    
'''
    - x in s, x not in s
    다른 프로그래밍 언어에선 쉽게 볼 수 없는 조건문 제공.
    x in 리스트/튜플/문자열 : x가 리스트/튜플/문자열에 있을 때 true,
    x not in 리스트/튜플/문자열 : x가 리스트/튜플/문자열에 없을 때 true
    

'''

print(1 in [1,2,3])
print(1 not in [4,6,7])
print('j' not in 'python')

# 만약 주머니에 돈이 있으면 택시를 타고, 아니면 걸어가라
pocket = ['paper', 'cellphone','money']
if 'money' in pocket :
    print("축하합니다! 당장 택시를 타세요!")
else : 
    print("택시는 얼어죽을놈의 택시여 걸어가라")
    
'''
    - 조건문에서 아무것도 수행을 안하고 싶을 때 사용하는 키워드 : pass
    if 'money' in pocket :
        pass
    else :
        print("카드를 꺼내요")
'''


'''
    2. 다양한 조건을 판단하는 elif문 
    else if와 같은 놈.
    
    "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면
    택시를 타고, 돈도 없고 카드도 없으면 걸어가라."


'''
pocket = ['paper','headphone']
if 'money' in pocket :
    print("택시를 타세요.")
# elif 'money' not in pocket and 'card' in pocket :
## elif는 이전 조건문이 거짓일 때 수행된다.
elif 'card' in pocket : ## 현재 돈은 없는 상태. 굳이 명시해줄 필요는 없다.
    print("택시를 타세요")
else :
    print("걸으쇼")
    
    
'''
    3. 조건부 표현식
    if score > 60 : 
        message = "success"
    else : 
        message = "failure"
        
    이 문장을 파이썬의 조건부 표현식으로 사용하면 다음과 같이 바꿀 수 있다.
    
    message = "success" if score >=60 else "failure"
    
    >> 즉, "조건문이 참인 경우 행동" if 조건문 else "조건문이 거짓인 경우 행동"
    
    가독성에 유리하고 한 줄로 작성할 수 있어 좋음.
    

'''
    


########################################################################
'''
    <조건/제어문 : while>
    1. while문의 기본 구조
        while 조건문 :
            수행문장1
            수행문장2
            수행문장3
            ....


'''
treeHit = 0;
while treeHit<10 :
        treeHit = treeHit+1
        print('지금까지, {0}번 찍었습니다.'.format(treeHit))
        if treeHit == 10 :
            print("나무 넘어가요 ^^~")
            
'''
    2. while문만들기
    여러가지 선택지 중 하나를 선택하여 입력받는 예제

'''
'''prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter your number : 
"""

number = 0
while(number != 4) :
    print(prompt)
    number = int(input()) ## 형변환
    
'''
'''
    3. while문 강제로 빠져나가기
    break문을 사용하자.

'''
coffee = 10
money = 300
print("{0}원 받았습니다. 커피를 내립니다.".format(money))
while money :
    coffee -=1    
    print(f'남은 커피의 양은.... {coffee}입니다.')
    if coffee == 0 :
        print('재료 소진, 판매를 중지합니다.')
        break
    

'''coffee = 10
while True :
    money = int(input("돈을 넣어주세요 : "))
    if money == 300 :
        print("커피를 내립니다.")
        coffee-=1
    elif money > 300 :
        print("거스름돈 {0}를 주고 커피를 내립니다.".format(money-300))
        coffee-=1
    else : 
        print("돈은 돌려드릴게요. 다른 곳 가서 마시세요.")
        print("남은 커피의 양은 {0}잔 입니다.".format(coffee))
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    '''
    
'''
    4. while문의 맨 처음으로 돌아가기
    continue 구문을 이용한다.
    
    5. 무한 루프
    조건식 부분에 true를 주면 된다.


'''
    
'''
    <제어 및 조건 : for문>
    1. for문의 기본 구조
    for 변수 in 리스트(튜플, 문자열 등..) : 
        수행할 문장 1
        수행할 문장 2
        ...


'''

'''
    1. 예제로 for문 이해하기
    
'''
## 1번, 전형적인 for문
test_list = ['one','two','three']
for i in test_list :
    print(i)
    
## 2번, 다양한 for문의 사용
a=[(1,2), (3,4), (5,6)]
for(first,last) in a :  ## 리스트의 요소값이 튜플값이므로, 자동으로 first, last안으로 들어간다.
                        ## 2장에 나옴. 튜플을 사용한 변수값 대입 방법을 참조
    print(first+last)
    
## 3번, for문의 응용
# 총 5명의 학생이 시험을 보았다. 시험 점수가 60점이 넘으면 합격, 그렇지 않으면 불합격.
# 합격인지 불합격인지를 나타내라.
marks = [90,25,67,45,80]
number = 0
for mark in marks :
    number += 1 ## 인덱스값을 따로 참조할 수 있는 방법이 없다보니... 밖에서 선언해서 가져왔음.
    if mark >= 60 :
        print("%d번 학생은 합격입니다." % number)
    else :
        print(f'{number}학생은 불합격입니다.')
        
        
'''
2. for문과 continue
    while문에서처럼 사용이 가능하다.

'''
number = 0
for mark in marks :
    number += 1
    if mark < 60:
        continue
    print("%d번 학생, 축하합니다! 합격입니다." % number)
    
    
'''
    3. for문과 함께 사용되는 range 함수
    range 함수 : 숫자 리스트를 자동으로 생성해주는 함수
    
    a = range(10) > 0부터 10 미만의 숫자를 포함하는 range 객체를 생성해준다.
    시작 숫자와 끝 숫자를 지정하려면 range(시작숫자, 끝숫자)형태를 사용하는데,
    끝 숫자는 들어가지 않는다.
    
'''

# range 함수의 예시
add = 0
for i in range(1, 11) :
    add = add + i
print(add) ## 1~10까지 합인 55를 뱉어낸다.


marks = [90,25, 67, 45, 80]

for number in range(len(marks)) :
    if marks[number] < 60 :
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
    
    
# for와 range를 이용한 구구단
for i in range(2, 10) :
    for j in range (1, 10) :
        print(i*j, end=" ")
    print('')
    
'''
    print()만 쓰면 newline으로 들어가기 때문에, 줄바꿈이 된다.
    매개변수 end를 넣어준 이유는, 그것을 막기 위함이다.
    결과값을 출력할 때 다음 줄로 넘기지 않고 그 줄에서 계속해서 출력하기 위해서이다.
    
'''


'''
    4. 리스트 내포 사용하기
    리스트 안에 for 문을 포함하는 리스트 내포를 사용하면 
    편리하고 직관적인 프로그램을 생성가능하다.
    

'''
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

## 이거 받고, if 조건도 사용이 가능하다. 짝수만 3을 곱해보자.
## 곱해진 놈들만 추가된다.
result=[num*3 for num in a if num%2==0]
print(result)

'''
    - 리스트 내포의 일반적인 문법
    [표현식  for 항목 in 반복가능한 객체 if 조건문]
    for문을 2개 이상 사용할 경우 다음과 같이 표현한다.
    [표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]
    밑으로 갈 수록 들여쓰기 되는 놈들이라고 생각하면 된다.
    
    만약 구구단의 모든 결과를 리스트에 담고싶다면, 다음과 같이 리스트 내포를 사용해보자.
'''

result = [i*j for i in range(2,10)
              for j in range(1, 10)
          ]
print(result)