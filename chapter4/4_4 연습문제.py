# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(n):
    if n%2==0 :
        print("짝수")
    else :
        print("홀수")
'''
    람다 + 조건부 표현식 사용
    is_odd = lambda x : True if x%2 == 0 else False
    is_odd(3)

'''
# is_odd(int(input("숫자를 입력하세요")))

#Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg(*args) :
    sum = 0
    for i in args : 
        sum+=i
    print(sum/len(args))


avg(1,2,3,4,5,6,7,8,9,10)


#Q3 오류 수정
# input1 = int(input("첫번째 숫자를 입력하세요:"))
# input2 = int(input("두번째 숫자를 입력하세요:"))

# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)

#Q5 
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.flush() ## 이 문장을 추가해주자. > 버퍼에 남겨져있는데 close를 안해줘서 그런듯
           ## 아니면 f1.close()를 해주든지
f2 = open("test.txt", 'r')
print(f2.read())
f1.close()
f2.close()
#Q6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 
# (단 프로그램을 다시 실행하더라도 
# 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
'''
    close를 명시적으로 할 필요가 없는 with 구문 
    with open("test.txt", "w") as f1:
        f1.write("Life is too short!")
    with open("test.txt", "r") as f2:
        print(f2.read())

'''
f1 = open('text.txt','a',100,'UTF-8')
while True :
    inputStr = input("입력하세요 >> ")
    f1.write(inputStr+"\n")
    if(inputStr) :
        break
f1.close()

f1=open('texttest.txt', 'r')
inputStr = f1.read()
inputStr = inputStr.replace('java', 'python')
print(inputStr)