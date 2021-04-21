import random
# 자료형 반환하는 함수 type()
# 변수에 자료형을 지정하지 않고 넣는경우
x = 3
print(type(x))

# 변숭에 자료형을 지정하여 넣는 경우 -> 생성자함수사용
x = int(20)
y = complex(1j)
z = frozenset(('math','science','computer'))

print(x,type(x))
print(y,type(y))
print(z,type(y))

#서로 형변환 가능
# y = int(y) -> 복소수는 정수형이나 실수형으로 변환 불가 문자열은 가능
print(y)

#random 모듈을 통한 난수 생성
x = random.randrange(1,100)
print(x)