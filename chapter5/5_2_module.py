'''
    1. 모듈이란
        함수나 변수, 클래스를 모아놓은 파일.
        파이썬 프로그램에서 불러와 사용할 수 있게끔 파이썬 파일이라고 할 수 있다.
        
    2. 모듈 만들기
        걍 파이썬 파일 하나 만드는거임
        작업영역에서 import 파일이름 하면 됨. .py 떼고
        
'''

import moduletest # 숫자가 먼저 들어가면 안되나봐... 아님 언더바가 안되나?

## print(moduletest.powww(10,10))
'''
    import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있음.
    파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 모듈을 말함.
    
    때로는 moduletest.poww말고 그냥 poww로 쓰고 싶을 수 있는데, 이 땐
    
    'from 모듈 이름 import 모듈 함수'구문을 사용하면 된다.
    모듈 함수에 *를 사용해도 좋다.
'''


'''
    3. if __name__ == "__main__"의 의미
        moduletest함수에 print문을 두 개 추가했더니
        import 하는 순간에 추가한 print문이 실행되었다.
        이런 문제를 막기 위해서는 
        if __name__ == "__main__"을 실행해주어야 한다.
        

'''
print(moduletest.mult(1,3))

'''__name__ 변수?
    파이썬 내부적으로 사용하는 특별한 변수 이름.
    직접 실행하는 파일의 경우, 각 파일마다 할당되어있는 __name__ 변수에는 __main__값이 저장된다.
    
    하지만 파이썬 셸이나 다른 파이썬 모듈에서 moduletest를 import 할 경우,  
    __name__변수에는 moduletest의 값이 저장된다.

'''

'''
    클래스나 변수등을 포함한 모듈
    moduletest2.py
    
    

'''

import moduletest2

print(moduletest2.PI) ## 그냥 쓰면 됨

'''
다른 파일에서 모듈 불러오기
이거는 사이트를 보자
wikidocs.net/29


'''