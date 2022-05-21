
from unittest import result


class Calculator :
    def __init__(self):
        self.result = 0
    def add(self, num ):
        self.result += num
        return self.result
    # 빼기 기능을 원한다면 여기에 함수를 추가하면 된다.
    def sub(self, num) :
        self.result -= num
        return self.result
    
    
'''
    사칙연산 클래스 생성 : + - * /
    name : FourCal()
    func : setData(a,b) return X
           add() return a+b
           mul() return a*b
           sub() return a-b
           div() return a/b
'''

class FourCal() :
    # 객체에 숫자 지정할 수 있게 만들기
    # 생성자
    def __init__(self, first, second) :
        self.first = first
        self.second = second
    # 메서드
    def setdata(self,first,second) :
        # 매개변수로 self를 받는데, 이는 특별한 의미를 가짐.
        '''
            첫 번재 매개변수는 관례적으로 self를 사용한다.
            객체를 호출할 때 호출한 객체 자신이 전달되므로 self를 사용한 것이다.
            self 말고 다른 이름을 사용해도 좋다.
            
            어쨌든 self를 명시적으로 구현하는 것은 파이썬만의 특징이다.
        
        '''
        '''
            ** self와 관련된 메서드의 호출방법
            클래스를 통해 메서드를 호출하는 것도 가능하다.
            클래스 이름.메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 한다.
            
            객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.
        
        '''
        self.first = first
        self.second = second
        '''
            self == 전달된 a 객체
            즉, a.first / a.second라고 봐도 무방하다
        '''
        
        
        # 더하기 기능
    def add(self) :
        result = self.first + self.second
        return result
        
    def mul(self) :
        result = self.first * self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result
        
    def sub(self) :
        result = self.first - self.second
        return result



a = FourCal(10,10)
print(type(a)) # __main__.FourCal 
               # type : 파이썬의 내장 함수. 객체 타입을 출력
               
               

'''
    클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다. 
    클래스에서는 이 부분을 이해하는 것이 가장 중요하다.
'''
#a.setdata(1,2)
print(a.first,a.second)
print(a.add(), a.sub(), a.div(), a.mul())
b = FourCal(20,20)
#b.setdata(3,4)
print(b.first,b.second)
print(b.add(),b.sub(),b.div(), a.mul())


'''
    생성자
    FourCal 클래스에 setdata()를 수행하지 않으면
    오류가 발생한다. 
    객체에 초깃값을 설정하기 보다는 생성자를 구현하는 것이
    더 안전한 방법이다.
    생성자란, 객체가 생성될 때 자동으로 호출되는 
    메서드이다.
    
    사용법 : def __init__(self,first,second) :
                    codes....
                    
    __init__메서드도 다른 메서드와 같이 첫 번째 매개변수에 self가 자동으로 전달된다.

'''


'''
    클래스의 상속
    FourClass를 상속받아 구현해보자
    - 형태
    class MoreFourCal(FourCal) :
        pass
    
    >> class className(inherit ClassName)
    괄호 안에 상속할 클래스의 이름을 넣어주면 됨.
    
    
    - 이유
    기존 클래스를 변경하지 않고 기능을 추가하거나 
    기존 기능을 변경하려고 할 때 사용

'''

class MoreFourCal(FourCal) :
    def pow(self) :
        result = self.first ** self.second
        return result
    
c = MoreFourCal(4,2)
print(c.pow())


'''
    메서드 오버라이딩
    FourCal 객체에 4,0을 설정하고 div 메서드를 호출하면 4를 0으로 나누려고 
    하므로 ZeroDivisionError가 발생한다.
    0으로 나눌 때 오류가 아닌 0을 돌려주도록 만들고 싶다면....
    
    >> 오버라이딩 한다.

'''

class SafeForCal(FourCal) :
    def div(self) :
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second
        
    
'''
    부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩이라고
    한다.
    이렇게 오버라이딩 되면 부모의 메서드 대신 오버라이딩한 메서드가 호출된다.
'''

'''
    클래스 변수
    객체 변수는 다른 객체들에 영향을 받지 않고 독립적으로 그 값을 유지한다.
    그러나 클래스변수는 이와 성격이 좀 다르다.
    
'''

class Family : 
    lastname = 'kim' # 클래스 변수의 선언

print(Family.lastname)
# 다음과 같이 객체를 통해서도 접근이 가능하다
print(Family().lastname)

Family.lastname = 'Park'
print(Family.lastname)
print(Family().lastname)
# 클래스 변수를 바꾸면, 전체가 바뀐다.(객체로 참조해도)
# 클래스로 만든 모든 객체에 공유됨

a = Family()
a.lastname = "Jeong"
print(a.lastname) ## jeong
print(Family.lastname) ## park
'''
    Family 클래스의 lastname이 바뀌는 게 아니라
    a 객체에 lastname이라는 객체 변수가 새롭게 생성된다.
    a.lastname : Family class의 lastname이 아니라 객체
    a의 lastname을 가리킨다.
    
    Family 클래스의 lastname 클래스변수 값은 바뀌지 않는다.
    
'''

