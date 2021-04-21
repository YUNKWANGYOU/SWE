a = ['Oragne','pineapple','Kiwi','banana']
tmp = a

# 오름차순 정렬
tmp.sort()
print(a)

# 내림차순 정렬
tmp.sort(reverse=True)
print(a)

#사용자 정의 함수로 목록 정렬
#50과의 거리가 가장 작은것부터오름차순
def func(n):
    return abs(n-50)
b =[100,40,65,82,23]
b.sort(key = func)
print(b)

# 일반적으로 정렬 함수는 대문자가 소문자 앞에옴, 따라서 lower함수를 사용하면 구분없이 정렬됨
tmp = a
tmp.sort(key = str.lower)
print(tmp)
# 그렇다면 대문자 함수를 서도 마찬가지일 것이다.
tmp.sort(key = str.upper)
print(tmp)

# copy 함수는 복사하기위함 (의도는 잘 모르겠음)
tmp2 = a.copy()
print(tmp2)