x = 5 
y = "yunkwang"
z = 3.0
X = 4
# x != X
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(X,type(X))

# camel case
sweStuent = 'yunkwang'
# pascal case
SweStudent = 'yunkwang'
# snake case
swe_student = 'yunkwang'

# multi value assignment
a,b,c = 'chocolate',4,'study'
d=e=f='WeAreSame'
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,e,f,type(d),type(e),type(f))

# 리스트 값이 하나씩 들어감 (양쪽 개수 안맞으면 value error 발생)
study = ['swe','basketball','baseball']
l,m,n = study
print(l,type(l))
print(m,type(m))
print(n,type(n))

# 문자열에 +를 사용하면 문자열이 합쳐짐(숫자와 문자를 결합하여 출력하면 오류가 발생)
a = 'Hello'
b = 'Dongguk'
print(a+b)

# global/local variable

# a가 local variable이기 때문에 함수안에서 사용 가능
a = 'Hi '
def func():
    print(a+'Dongguk')
func()

def func2():
    i = 'Bye '
func2()
# print(i+'Dongguk')을 실행해보면,
# i는 local variable이므로 오류 발생

# 해결할 수 있는 방법은 global 예약어의 사용
def func3():
    global i 
    i = 'Bye '
func3()
print(i + 'Dongguk')
