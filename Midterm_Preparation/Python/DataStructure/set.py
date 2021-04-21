# Set은 튜플, 리스트와 달리 index가 생성되지 않는다.
# 대입연산자를 통해 set을 생성
a = {'math','science','computer'}
print(a,type(a))
# 생성자를 통해 set 생성
b = set(('math','science','computer'))
print(b,type(b))

# 중복을 허용하지 않기 때문에, 중복되는 항목이 있다면 하나만 남기고 지워진다.
a = {'math','science','computer','math'}
print(a,type(a))

# index가 없기 때문에 접근이 불가능하다.
print(a[1])