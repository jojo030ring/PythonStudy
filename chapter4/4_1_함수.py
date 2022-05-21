''' 
    1. 파이썬 함수의 구조
    def 함수명(매개변수):
        수행할 문장 1
        수행할 문장 2
        수행할 문장 3
        ...
    
    def : 함수를 만들 대 사용하는 예약어
    함수 이름은 함수를 만드는 사람이 임의로 생성 가능
    


'''
# def add() :
#     inputStr = input("숫자를 두 개 입력하세요").split(" ")
#     return int(inputStr[0])+int(inputStr[1]) ## number는 숫자가 아닌 문자열임을 주의하자.

# print(add())

'''
    2. 매개변수와 인수
    매개변수 : 함수를 정의할 때 받는 값을 정의한 것
    인수 : 함수를 호출할 때 함수에 전달해줄 값

    3. 입력값과 결과값에 따른 함수의 형태
    함수는 들어온 입력값을 받아 어떤 처리를 하여 적절한 결과값을 돌려준다
    입력값 => 함수 => 결과값

    - 일반적인 함수
    입력값이 있고 결과값이 있는 함수가 일반적인 함수.
    def add(a,b) : 
        result = a+b
        return result

    - 입력값이 없는 함수
    def say() :
        return 'hi'

    - 결과값이 없는 함수
    def add(a,b) :
        print("%d, %d의 합은 %d입니다." % (a,b,a+b))
    
    억지로 이 함수를 변수에 담으면, 거짓을 나타내는 "none"이 출력된다.
    - 입력값, 결과값이 모두 없는 함수
'''

from re import I


def isRealNone(a,b):
    print("%d %d" % (a,b))

c=isRealNone(10,20)
print(c)

'''
    4. 매개변수 지정하여 호출

'''
def add(a,b):
    return a+b

result = add(a=3, b=7) ## a에 3을, b에 7을 전달함
print(result)
result = add(b=7, a=3)
print(result)

'''
    매개변수를 지정하면, 순서에 상관 없이 사용할 수 있다는
    장점이 있다.

'''


'''
    5. 입력값이 몇 개가 될지 모를 때는 어떻게 해야하는가?
    def 함수이름(*매개변수):
        <수행할 문장>
        ...
    
    일반적으로 볼 수 있는 함수의 형태에서 괄호 안의 매개변수가 *매개변수로 대체되었을 뿐.

    - 여러 개의 입력값을 받는 함수를 생성하기

'''
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5,6,7,8,9,10)) ## 55를 리턴함

'''
    *arg처럼 매개변수 이름 앞에 *를 붙이면 입력 값을 전부 모아
    튜플로 만들어준다. 
    위와 같은 경우라면 (1,2,3,4,5,6,7,8,9,10)으로 변경된다.
    arg는 임의로 정한 변수의 이름이므로 원하는 이름으로 바꿀 수 있다.

    여러 개의 값을 처리할 때 def add_many(*args)처럼 함수의 매개변수로 *args만 들어갈 수 있는 것은 아니다.
'''

def add_mul(choice, *args):
    result = 0
    if choice == "add":
        for i in args:
            result += i
    
    elif choice == "mul":
        result = 1
        for i in args:
            result *=i
    return result

print(add_mul("add",1,2,3,4,5))
print(add_mul("mul",1,2,3,4,5))
 
'''
    매개변수 choice에 'add'가 입력된 경우, *args에 입력되는 모든 값을 더해
    15를 돌려주고, 'mul'이 입력된 경우 *args에 입력되는 모든 값을 곱해서 120을 돌려줌

'''

'''
    *** 키워드 파라미터 kwargs
    사용 : 매개변수 앞에 **를 두 개 붙인다.

'''
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
## {'a': 1}
print_kwargs(age=3, name='foo')
## {'age': 3, 'name': 'foo'}

'''
    입력값이 모두 딕셔너리로 변경되어 들어간다.

    ** : 입력값이 딕셔너리로 변경됨
    * : 입력값이 튜플로 변경됨

    kwargs는 keyword arguments의 약자, args와 마찬가지로 관례적으로 사용됨.
'''


'''
    6. 함수의 결과값은 언제나 하나!

    def add_and_mul(a,b) :
        return a+b, a*b
    
    이런 함수가 있다고 치자. 이는 자바나 c언어 등의 문법에선 .. 절대 
    허용되지 않는 문법이다. 하지만 파이썬에서는 쌉가능

    이유 : 튜플값 하나인 (a+b, a*b)로 돌려주기 때문
    결국 튜플에 담으면 리턴값은 한 개가 되는 것이다.

    만약, 이 하나의 튜플값을 2개의 결과값처럼 받고싶다면, 
    다음과 같이 하면 된다.

'''

def add_and_mul(a,b) :
    return a+b, a*b

i,j = add_and_mul(10,20)
print(i,j)
'''
    튜플의 특성에서 나왔던 부분이다. 
    각각의 변수에 튜플 값을 삽입할 수 있다고 했다.
    i = 10, j = 20이 된다.

    그리고 아예 return문을 두 개 쓰는 경우가 있는데,
    함수는 return문을 만나는 순간 결과값을 돌려준 뒤 바로 함수를 빠져나가기 때문에
    소용이 없다.

'''

'''
    * return의 또다른 쓰임새
    특별한 상황일 때 함수를 빠져나가고 싶다면, return을 단독으로 사용하여 즉시
    빠져나갈 수 있다.

'''
def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s 입니다.' % nick)
say_nick('바보')
say_nick('천재')


'''
    7. 매개변수에 초기값 미리 설정하기 : 기본값
    초기값을 설정해주고 싶은 매개변수에 매개변수=값
    형태로 넣어주면 된다.
'''

def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.' % name)
    print('나이는 %d 입니다.'% old)
    if man :
        print("남자입니다.")
    else : 
        print('여자입니다.')

say_myself('박응용', 27, False)
say_myself('박응용',28)

'''
    주의점 : 기본 매개변수는 반드시 끝에 넣어주어야 한다.
    def say_myself(name, man=True, old):
    
    say_mysqlf('박응용',27)로 호출한다면
    name=박응용으로 잘 들어가지만, 파이썬 인터프리터는 27을 
    man변수와 old 변수 중 어느곳에 대입해야하는지 알 수 없게 된다.

    그래서 꼭... 초기화 시키고 싶은 매개변수는 항상 뒤쪽에 배치하도록 해야한다.
'''


'''
    8. 함수 안에서 선언한 변수의 효력 범위

    a = 1
    def vartest(a):
        a = a +1

    vartest(a)
    print(a)

    함수 안에서 사용하는 변수의 이름을 밖에서도 동일하게 사용한다면, 
    함수 안에서 사용하는 변수는 함수 안의 변수이므로 함수 밖의 변수가 출력되게 된다.

    즉, 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다는 뜻이다.
    
    ** 매개변수로 줘도요?
    ㅇㅇ. 이미 매개변수로 주고 있잖슴
    매개변수로 복사되는 값은 call by value라서 함수 밖의 변수를 변화시킬 수도 없다..
    
    
    '''



'''
    9. 함수 안에서 함수 밖의 변수를 변경하는 방법
    1) return 사용하기
    
'''
a = 1
def vartest(a) :
    a+=1
    return a

a= vartest(a)
print(a)

'''
    2) global 명령어 사용하기

'''
a = 1
def vartest() :
    global a
    a+=1
    return a

a= vartest()
print(a)
'''
    global a는 함수 밖의 a 변수를 직접 사용하겠다는 뜻임.

    사용 안하는게 좋다. 함수는 독립적으로 존재하는 것이 좋기 때문.
    외부 변수에 종속적인 함수는 좋은 함수가 아니다.
    그러므로 지양하고, 첫 번째 방법을 사용하자.

'''

'''
    10. lambda
    함수를 생성할 때 사용하는 예약어.
    def와 동일한 역할을 한다. 함수를 한 줄로 간결하게 만들 때 사용한다.
    
    사용법 : lambda 매개변수1, 매개변수2, 매개변수 3,.... : 매개변수를 이용한 표현식

'''

add = lambda a, b:a+b
result = add(3,4)
print(result)

## 다음과 같다.

def add(a,b) :
    return a+b

result = add(3,4)
print(result)
'''
**** lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려준다.
'''