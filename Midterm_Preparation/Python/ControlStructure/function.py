# Python 함수의 이용
#함수 원형
def func():
    print('a')
func()

#함수에 매개변수(parameter) 전달.
def func2(a) :
    print(a)
func2('yunkwang')
func2('yejin')
func2('hey')

# 함수가 지정하는 인수의 수와 호출할 때 넣는 인수의 수가 같아야함
def func3(a,b,c):
    print(a,b,c)
func3('a','asdfasf','asdf')
# func3('a','b') -> 오류남

# 함수에 전달 될 인수의 수를 모르는 경우 매개변수 앞에 * 추가
def func4(*a):
    print(a[1])
func4('a','asdfasf','asdf')

# key = value 구문을 이용하여 매개변수를 전달할 수도 있다.
def func5(x,y,z):
    print(x,y,z)
func5(z = 'yunkwang', x = 'hello', y = 'sexy')

# key = value로 전달하는 인수의 수를 모르는 경우 매개변수 앞에 ** 추가
# 배열에서 불러올 때 ''를 붙여서 불러와야함
def func6(**x):
    print(x['b'])
func6(a = 'yunkwang', b = 'hey')

# default parameter value : 매개변수의 default 값을 정해놓는다.
def func7(a = 'yunkwang'):
    print(a)
func7()

# 문자열, 숫자, list, dictionary 등을 인수로 보낼 수 있다.
def func8(a):
    for i in a :
        print(i)
b = ['math','science','computer']
func8(b)

# 함수가 값을 반한하도록 하려면 return문 사용
def func9(a):
    return a*5
print(func9(3))

# pass
def func10():
    pass

# 재귀함수
def func11(a):
    if a > 0 :
        print(a)
        return func11(a-1)
    else :
        return 0
func11(10)