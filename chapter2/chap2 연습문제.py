# Q1
score = {"국어":80, "영어":75, "수학" : 55}
output = format((score["국어"]+score["영어"]+score["수학"])/3.0, "0.3f")
print(output)

#Q2
if 13 % 2 != 0 : 
    print("홀수")
else : 
    print("짝수")
    
#Q3
mrHong = "881120-1068234"
year = "19"+mrHong[0:2]
month = mrHong[2:4]
day = mrHong[4:6]

print(year,month,day,sep=":")

#Q4
sex = mrHong[-7]
if sex=='1' : 
    print("남자")
else :
    print("여자")

#Q5
a = "a:b:c:d"
print(a.replace(":","#"))


# Q6
lists = [1,3,5,4,2]
lists.sort()
lists.reverse() ## 큰 수가 아니라 그냥 인덱스에 할당된 요소들을 거꾸로 배열하는구나...
print(lists)


# Q7
#  다시

# Q8
tuples = 1,2,3
lists = list(tuples)
lists.append(4)
print(tuple(lists))

tuples = 1,2,3
tuples=tuples + (4,)
## 튜플이 변경되는 것이 아닌, 새로운 튜플이 생성되는 것을 의미 >> 투플도 합집합 쓸 수 있구나...
print(tuples)


# Q9
## 3번. key값은 불변성을 가지고 있어야 하는데 불변성을 가지고 있지 않은 요소가 3번임.

# Q10
a={'A':90, 'B':80,'C':70}
##두 가지 방법 > get을 이용하든지 인덱스처럼 이용하든지
elemB = a.get('B') ## 없으면 none
if elemB :
    print(elemB)
else :
    print("error")
    
# Q10
a={'A' : 90, 'B':80, 'C':70}
print(a.pop('B'))


# Q11
a=[1,1,1,2,2,2,3,3,3,4,4,4,5]
print(set(a))


# Q12
a=b=[1,2,3]
a[1]=4
print(b)
'''
    a,b 변수는 모두 동일한 [1,2,3] 이라는 리스트 객체를 가리키고 있으므로..

'''