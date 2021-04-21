# 리스트를 선언하는 여러가지 방법
a = ['math','science','english']
b = list(('math','science','english'))
c = ['math','science','english','math']

print(a,b,c)

# 여러 자료형 가능
a = [1,'math',3.0]
for i in a :
    print(i,type(i))

# 음수 인덱싱 가능
print(a[-1])

# 저장한 항목이 목록에 있는지 확인
if 1 in a :
    print("Im here.")

# 저장된 항목값 변경
a[0:2] = ['I\'m changed.','I\'m changed too']
print(a)

# 리스트 결합
b = ['Appended','appended2']
a = a+b
print(a)

# 지정된 인덱스에 삽입
a.insert(1,'Im inserted')
print(a)

# 지정해준 요소 제거
a.remove('Im inserted')
print(a)

# 지정해준 인덱스의 요소 제거(인덱스 지정안할 경우 마지막 항목 제거)
a.pop(1)
print(a)
a.pop()
print(a)

# 지정해준 인덱스의 요소 제거
del a[2]
print(a)

# 전부 빙워버리기
a.clear()
print(a)