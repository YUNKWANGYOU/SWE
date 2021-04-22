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
# print(a[1]) -> 에러

# set의 길이 추출
print(len(a))

# set은 add 메소드로 항목 추가 가능
a.add(1)
print(a)

# update()메소드를 이용하여 다른 set의 항목을 현재 set에 추가 ( 중복되면 알아서 삭제됨 )
b = {'algorithm','swe','math'}
a.update(b)
print(a)
# 이 때, update메소드 안의 매개변수로는 tuple, list, dictionary 모두 가능하다.

# remove(parameter) 메소드를 이요하여 항목을 제거한다. remove 메소드의 특징은 항목이 없다면 오류가 발생한다.
a.remove('swe')
print(a)

# discard(parameter) 메소드를 이요하여 항목을 제거한다. discard 메소드의 특징은 항목이 없다면 무시한다.
a.discard('ralgorithm')
a.discard('math')
print(a)

# pop()을 이용하여 항목을 제거한다. 별도의 index가 없으므로 제거되는 항목을 알 수 없다.
# 몇 번 실행해봐도 pop() 메소드로부터 같은 결과가 나오는 것을 보면, 주소를 참조하는 것 같다. 하지만 이조차 알 수 없긴하다.
print(a.pop())
print(a)

# clear()
a.clear()
print(a)

#Combine Sets
# union() 메소드는 합집합 set을 return 해준다.
a = {'a','b','c','d'}
b = {'c','d','e','f','math'}
c = a.union(b)
print(c)

# update() 메소드는 메소드를 사용하는 객체가 매개변수를 삽입한다. 
a.update(b)
print(b)

# 결과적으로 union(), update(), + 는 사용방법은 다르지만 같은 결과를 불러올 수 있다.

# intersection_update()메소드는 중복된 항목만 유지시킨다.
a = {'a','b','c','d'}
a.intersection_update(b)
print(a)

# intersection() 메소드는 중복된 항목만 유지시킨 집합을 반환시킨다.
a = {'a','b','c','d'}
c = a.intersection(b)
print(c)

#symmetric_difference_update() 메소드는 두 집합에 없는 항목만 유지시킨다.
print(a,b)
a.symmetric_difference_update(b)
print(a)
a = {'a','b','c','d'}
b.symmetric_difference_update(a)
print(b)
# 결과는 같다. (A-B or B-A 가 아닌 합집합에서 교집합만 뺀 모양을 기억하자.)

#symmetric_difference() 메소드는 두 집합에 없는 항목만 반환시킨다.
a = {'a','b','c','d'}
b = {'c','d','e','f','math'}
c = a.symmetric_difference(b)
print(c)