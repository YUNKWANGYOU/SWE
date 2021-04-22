# Python에서는 list를 array대신 사용한다.
# 선언
a = ['math','science','computer']
# 접근
b = a[0]
print(b)
# 길이
print(len(b))
# for 문 활용
for i in a:
    print(i)
#요소 추가
a.append('algorithm')
print(a)
# 요소 제거 - pop(index)
a.pop(1)
print(a)
# 요소 제거 - remove(요소)
a.remove('math')
print(a)