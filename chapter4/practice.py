def func1(*pram):
    result = 0
    for tmp in pram :
        result += tmp
    
    print(result)
    
func1(1,2,3,4,5,6,7,8,9,10)

def print_kwargs(**kwargs) :
    print(kwargs)
    
print_kwargs(name='foo', age='3')

add = lambda a, b : a+b
print(add(3,4))