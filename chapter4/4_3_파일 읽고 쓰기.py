'''
    1. 파일 생성하기
    프로그램을 실행한 디렉터리에 새로운 파일이 하나 생성된다.

    사용법 : fileObj = open(fileName(Path), fileOpenMode)

    <파일 열기 모드>
    - "r" : 읽기모드, 파일을 읽기만 할 때 사용
    - "w" : 쓰기모드 파일의 내용을 쓸 때 사용
    - "a" : 추가모드 파일의 마지막에 새로운 내용을 추가시킬 때 사용
    
    쓰기모드 > 해당 파일이 존재할 경우, 원래 내용이 모두 삭제 
              해당 파일이 존재하지 않을 경우, 새로운 파일이 생성

    파일 이름에는 경로명을 사용할 수도 잇다.

    - f.close()
    f.close()는 열려있는 파일 객체를 닫아주는 역할을 한다.
    프로그램을 종료할 때 파이썬 프로그램이 자동으로 닫아주긴 하지만, 직접
    닫아주는 것이 좋다.

    쓰기모드로 열었던 파일을 닫지 않고, 다시 사용하려고 하면 오류가 발생하기 때문이다.

    *** 파일 경로와 슬래시 /
    - 파일 경로에 슬래시를 사용할 경우-
    C:/doit/새파일.txt
    - 역슬래시를 사용할 경우-
    C:\\doit\\새파일.txt
    또는,
    rC:\doit\새파일.txt 로 사용해야 한다.

    문자열 앞에 r문자(Raw String)을 덧붙여 사용해야 한다.
    왜냐면, 파일 경로에 \n같은 이스케이프 문자가 있는 경우
    줄바꿈 문자로 해석되는데,
    의도했던 파일의 경로와 달라지기 때문이다.
    

'''

'''
    2. 파일을 쓰기모드로 적어 출력값 적기

'''


f=open("./안녕하세요.txt", "w", 50, "UTF-8")
## 한국어 쓰면 깨져서 UTF-8로 지정해주었음.
for i in range(1,10) :
    data= "%d번째 줄입니다..." % i
    f.write(data+"\n")
## 버퍼 비울 때는 f.flush()
f.close()


'''
    3. 프로그램의 외부에 저장된 파일을 읽는 방법
    외부 파일을 읽어들여 프로그램에서 사용할 수 있다.
    1) readline함수 사용

'''
f=open("./안녕하세요.txt", 'r',50,"UTF-8")
line = f.readline()
print(line)
f.close()

## 모든 줄을 읽어서 출력하고 싶은 경우
f=open("./안녕하세요.txt", 'r', 50, "utf-8")
## utf-8을 지정해주었다면 읽어줄 때도 utf-8로 지정해주어야 한다.
while True :
    line = f.readline() # 더이상 읽어올 글자가 없을 때 ''(빈 문자열)를 리턴한다.
                        # 빈 문자열은 false였다.
    if not line: break
    print(line, end='') # 한 줄씩 읽어 출력할 때, 줄 끝에 \n이 있으므로, 빈 줄도 같이 출력된다.
                        # 그게 싫으면 end=''로 처리하면 된다.
f.close()


'''
    2) readlines 함수 사용
    파일의 모든 줄을 읽어 각각의 줄을 요소로 갖는 리스트를 돌려준다.
    
'''
f=open("./안녕하세요.txt", 'r', 50, "utf-8")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

'''
    *** 줄바꿈 문자 제거하기 (\n)
    >> strip() 함수를 사용하면 줄 바꿈 문자를 제거할 수 있음
'''
f=open("./안녕하세요.txt", 'r', 50, "utf-8")
lines = f.readlines()
for line in lines:
    print(line.strip()) # 줄 끝의 줄 바꿈 문자를 제거한다.
f.close()

'''
    3) read 함수 사용하기
    파일 전체의 내용을 문자열로 돌려준다. 따라서 아래 예의 data는 파일의 
    전체 내용이다.
'''
f = open('./안녕하세요.txt','r',50,'UTF-8')
data = f.read()
print(data)
f.close()



'''
    4. 파일에 새로운 내용 추가하기
    'a'모드로 열면 된다.

'''

f = open('./안녕하세요.txt', 'a',50,'UTF-8')
for i in range(10,20):
    data="%d번째 줄입니다..\n" % i
    f.write(data)
f.close()
## 10번째 부터 19번째까지의 줄이 추가되었음을 알 수 있음.

'''
    5. with 문과 함께 사용하기
    파일을 열면 항상 close 해주는 것이 좋다. 하지만 이렇게 파일을 열고 닫는 것이 자동으로 처리될 수 있다면, 
    몹시 편리할 것이다. 이 때 파이썬의 with문이 바로 이런 역할을 해준다.

    with open("./안녕하세요.txt", "w") as f :
        f.write("Life is too short, you need Python.")
    
    위와 같이 with문을 사용하면 with문을 벗어나는 순간 f객체가 자동으로
    close되어 몹시 편리함. 

'''

with open("./안녕하세요.txt","r",50,"UTF-8") as f : 
    for line in f.readlines() :
        print(line)