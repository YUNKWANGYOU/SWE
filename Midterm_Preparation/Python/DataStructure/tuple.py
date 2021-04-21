# tuple의 예 : tuple은 list 와 다르게 생성된 후에 항목을 변경, 추가, 제거할 수 없다.
# 대입연산자를 통한 튜플의 생성
a = ('math','science','computer')
# 튜플 생성자를 통한 튜플의 생성
b = tuple(('math','science','computer'))

# 튜플은 중복되는 항목을 추가할 수 없다.
# c = ('math','science','computer','math')

# 튜플 길이 반환
print(a,len(a))
print(b,len(b))

# 하나의 항목만 존재하는 튜플을 만들 때 ','기호를 붙인다. ',' 기호가 없다면 일반 문자열로 인식한다.
c = ('math',)
print(c,type(c))
d = ('math')
print(d,type(d))

# tuple도 list와 마찬가지로 여러 자료형을 넣을 수 있다.
e = ('math',1,3.0)
for i in e :
    print(i,type(i))

# index값으로 접근가능하다.
print(e[0])
# 음수 index도 가능
print(e[-1])

a = ('math','science','computer','algorithm','software')
# 시작과 종료 위치로 항목에 접근 가능하다.
print(a[2:5])

# 지정된 항목이 있는지 확인하기 위해 in 키워드를 활용한다.
if 'coomputer' not in a:
    print("Im not here")

# Tuple Update (리스트로 바꿔준 후 업데이트해주고 다시 튜플로 바꿔줌)
a = list(a)
a[1] = 'not science'
a = tuple(a)
print(a,type(a))

# 위와 같은 방법으로 remove,append가 가능하다.

# del 키워드를 이용하여 튜플 전체만 삭제할 수 있다.
del a
# print(a) -> 없으니 에러남


# Tuple Packing
a = ('math','science','computer')
# Tuple Unpacking (변수의 수 == 항목의 수 여야한다.)
x,y,z = a
print(x,type(x))
print(y,type(y))
print(z,type(z))

# Tuple Packing example2
b = ('math','science','computer','algorithm','software','game')
# Tuple Unpacking (변수의 수 != 항목의 수일 때 *은 한 번만 쓸수 있고 나머지 개수 맞춰서 들어가준다. )
x,*y,z,v = b
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(v,type(v))

# 두 개의 튜플 더하기
tmp = a+b
print(tmp,type(tmp))

tmp2 = (1,2,3,1)
print(tmp2)

