'''
    1. 사용자 입력
    - input의 사용
    - 프롬프트를 띄워 사용자 입력 받기

'''
a = input();
print(a)

number = int(input("숫자를 입력하세요 >> "))
print(number)

'''
    input() : 입력되는 모든 것을 문자열로 취급함.
    number는 숫자가 아니라 문자열이 된다.
    따라서 숫자로 사용하기 위해서는 int 함수등을 이용해야 한다.
'''

'''
    2. print 자세히 알기
    - ""로 둘러싸인 문자열은 +연산과 동일하다.
    - 문자열의 띄어쓰기는 , 로 한다
    - 한 줄에 결과값 출력하기 > end 매개변수
    

'''

#  1.
print("life" "is" "too" "short")
print('life'+'is'+'too'+'short') ## 두 결과가 동일하다.

# 2. 문자열 띄어쓰기는 콤마로 한다.
print("life","is","too","short")

# 3. 한 줄에 결과값 출력
for i in range(10) :
    print( i, end=' ')