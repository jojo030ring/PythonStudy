'''
    1. 불 자료형
    True / False만 가질 수 있음
    
    2. 자료형의 참과 거짓
    - "python" : 참
    - "" : 거짓
    - [1,2,3] : 참
    - [] : 거짓
    - () : 거짓
    - {} : 거짓
    - 1 : 참
    - 0 : 거짓
    - None : 거짓
    
    문자열, 튜플, 딕셔너리등 값이 비어있으면 거짓이 됨.("" / [] / () / {})
    
'''
a=[1,2,3,4]
while a :
    print(a.pop()) ## 4> 3> 2> 1 / 원소가 없어지면 거짓이 되니 while문을 빠져나오게 된다.
    
    
'''
    2. 불연산
    bool 내장함수를 사용하면 자료형의 참과 거짓을 식별 가능.

'''    
print(bool([1,2,3]))
print(bool(()))
print(bool(3))
    