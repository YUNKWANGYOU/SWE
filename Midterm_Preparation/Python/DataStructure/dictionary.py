# dictionary의 선언
a = {
    "brand" : "Apple",
    "model" : "iphone 12",
    "year" : 2020
    }

# dictionary의 접근
print(a['year'])

# 중복된 key값을 못갖는다 따라서 뒤에 오는 것을 덮어 사용한다.
a = {
    "brand" : "Apple",
    "model" : "iphone 12",
    "year" : 2020,
    "year" : 2021,
    True:"HI"
    }
print(a['year'])

# dictionary의 길이 확인
print(len(a))

# 다양한 자료형을 포함시킬 수 있다.
print(a[True])

# get()메소드를 이용하여 항목에 접근할 수 있다.
x = a['brand']
print(x)

# keys()메소드를 이용하여 모든 key 목록을 반환시킬 수 있다.
x = a.keys()
print(x)

# dictionary에 변경사항이 생기면 목록에 바로 반영한다.
a['name'] = 'yunkwang'
print(a)

# values()메소드를 이용하여 모든 value 목록을 반환시킬 수 있다.
x = a.values()
print(x)

# items() 메소드로 dictionary의 항목들을 tuple로 변환시킬 수 있다.
x = a.items()
print(x)

# key 이름을 참조하여 항목 값을 변경시킬 수 있다.
a['year'] = 2022
print(a)

# update 메소드를 이용하여 dictionary 항목을 update 할 수 있다. 이 때 매개변수는 한 쌍이상의 dictionary여야 한다.
# 없던 항목(key)은 추가한다.
a.update({'a':'b'})
print(a)

# pop(key)를 이용하여 항목을 제거한다.
a.pop('year')
print(a)

# popitem()을 이용하면 마지막으로 삽입된 항목을 제거한다.
a.popitem()
print(a)

# del 로도 삭제할 수 있다.
del a[True]
print(a)

# copy()메소드와 dict()메소드를 이용하여 dicitonary를 복사할 수 있다.
c = a.copy()
print(c)
d = dict(a)
print(d)

# dictionary 안에 dictionary를 추가할 수도 있다.

a = {
    'model' : 'iphone 11',
    'year' : 2019
}
b = {
    'model' : 'iphone 12',
    'year' : 2020
}
c = {
    'model' : 'iphone 13',
    'year' : 2021
}
d = {
    "phone a" :a,
    "phone b" :b,
    "phone c" :c
}

print(d)