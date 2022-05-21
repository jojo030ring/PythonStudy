'''
    1. 리스트를 복사하고자 할 때
    a = [1,2,3]
    b = a
    b는 a와 완전히 동일함.
    자바의 참조변수 개념이라고 생각하면 됨. 그냥 참조하는 변수가 하나 증가한 것 뿐
    이는 id함수, 즉 주소값을 리턴하는 함수를 써보면 알 수 있는데 둘이 주소값이 동일하다.
    아마 주소값을 복사한 게 아닐까.
    그리고 is 연산자로 a is b를 하게 되면 True 값이 나온다.
    즉, a와 b가 가리키는 객체는 같다는 것을 알 수 있다.

'''
a=[1,2,3]
b=a
print(str(id(a))+"/"+str(id(b)))
print(a is b)

'''
    a 리스트의 두 번째 요소를 변경했더니 a와 b 둘 다 똑같이 바뀌었다.
    a, b 모두 동일한 리스트를 가리키고 있기 때문이다.
    
'''
a[2]=100
print(a, b)

'''
    b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만들수는 없을까? 
    2가지 방법이 있다.
    
    (1) [:] 이용
    (2) copy 모듈 이용
'''
# 1번
a=[1,2,3]
b=a[:]
a[1]=4
print(a,b)

# a 값을 바꾸더라도 b리스트에는 영향을 주지 않음

# 2번
'''
    파이썬 모듈을 로드함.
    from copy import copy
'''
from copy import copy
a=[1,2,3]
b=copy(a)
print(a,b, b is a) ## false 리턴함

'''
    3. 변수를 만드는 여러가지 방법

'''

a,b = ('python','java') ## 튜플로 a, b에 값을 대입할 수 있다.
print(a,b,a,a,b) ## P J P P J
# 위 아래 예제 > 완전 동일
(a,b) = 'python','life'
print(a,b,a,a,b)
# 튜플은 괄호를 생략해도 된다.
# 리스트로 변수를 만들 수도 있다.

a=b='python'
print(a,a,b,b,b)


'''
    중요! 변수 간단히 바꾸기

'''

a=3
b=5
print(a,b)
a,b = b,a
print(a,b)