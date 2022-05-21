'''
    1.  딕셔너리란?
    사람은 누구든지 "이름" = "홍길동", "생일" = "몇 월 며칠" 등으로 구별할 수 있다. 
    파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 자료형을 가지고 있다. 
    요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데, 
    이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.
    
    - 딕셔너리 특징
    리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고
    Key를 통해 Value를 얻는다.
    
    2. 딕셔너리 생성법
    {Key1:Value1, Key2:Value2, Key3:Value3, ...}
    
    Key와 Value의 쌍 여러 개가 { }로 둘러쌓임
    각각의 요소는 Key : Value 형태로 이루어져 있고 
    쉼표(,)로 구분
    * key : 불변
    * value : 변함
    
    value에는 여러 자료형들이 들어갈 수 있음
    key에는 정수값도 들어갈 수 있음

'''
dic = {'name':'pay','phone':'0910301023','birth':'1111'}
print(dic)


a = {1:'hi'}
b = {'a' : [1,2,3]}
print(a)
print(b)

'''
    3. 딕셔너리 쌍 추가 / 삭제하기
    - 딕셔너리 쌍 추가
    a[key] = value


'''
a= {1 : 'a'}
a[3] = 'c'
print(a)

a['name'] = 'pey'
print(a)

a['list'] = [1,2,3]
print(a)

'''
    - 딕셔너리 요소 삭제하기
    del dic[key]
    >> list와 똑같음. 튜플은 삭제 삽입이 안되잖니
    dic.pop(key)

'''

del a['list']
print(a)

'''
    3. 딕셔너리를 사용하는 방법
    - 딕셔너리에서 key 사용해 value 얻기
    리스트,튜플, 문자열 : 요소값을 얻고자 할 때 인덱싱 / 슬라이싱 기법 중 하나. 
    딕셔너리 : key 값을 이용하여 value를 구해야함
    딕셔너리 변수이름[key]
    
    4. 딕셔너리를 만들 때 주의할 사항
    key 값은 고유한 값이므로 중복되는 key 값을 설정해놓으면 하나를 제외한
    나머지 것들이 모두 무시된다.
    a = {1:'a', 1:'b'}
    >> 1 : 'b'는 무시된다.
    
    key값으로 list는 쓸 수 없다. > 불변성이 없기 때문
    그러나, 튜플은 가능하다.
    
    5. 딕셔너리 관련 함수
    - 키 리스트 만들기 : keys()
'''
a={'name' : 'pey','phone' : '0119233452', 'birth' : '1118'}
print(a.keys())

'''
    파이썬 2.7 > a.keys()
    반환 값으로 dict_keys가 아닌 리스트를 돌려준다. 
    메모리 낭비가 발생
    
    파이썬 3 > dict_keys 객체
    다음에 소개할 dict_values, dict_items 역시 파이썬 3.0 이후 버전에서 추가된 것
    반환 값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다.
      
    dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도 
    기본적인 반복(iterate) 구문
    (예: for문)을 실행할 수 있다.
    리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
'''

'''
    - Value 리스트 만들기 (values)
    a.values()
    Key를 얻는 것과 마찬가지 방법으로 Value만 얻고 싶다
    >> values 함수를 사용하면 된다
    호출하면 dict_values 객체를 돌려준다

'''

print(a.values())



'''
    - key,value 쌍 얻기 : items()
    Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다
    
'''

print(a.items())

'''
    - key,value 모두 지우기 : clear()
    - key로 value 얻기 : dictionary.get(key)
'''
print(a.get('name'))
print(a.get('phone'))

'''
다만 다음 예제에서 볼 수 있듯이 a['nokey']처럼 
존재하지 않는 키(nokey)로 값을 가져오려고 할 경우 
a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 
None을 돌려준다는 차이가 있다. >> none은 거짓이라는 뜻
어떤것을 사용할지는 여러분의 선택이다.

'''
print(a.get('jotmang'))
# print(a['jotmang'])

'''
    - 해당 key가 딕셔너리 안에 있는지 조사하기 : in 연산자
    key in dictionary

'''