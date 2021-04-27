# Python의 람다 함수를 알아보자
x = lambda a : a+15
print(x(5))

x = lambda a,b,c : a+b+c
print(x(1,2,3))

# 람다함수는 다른 함수 내에서 익명함수로 사용될 때 유용하다.
# 하나의 인수를 사용하는 함수가 정의돼있고, 해당인수에 곱하는 숫자롤 동적으로 바꾸고싶을 때
def func(n):
    return lambda a : a*n

b = func(2)
print(b(7))
c = func(3)
print(c(3))