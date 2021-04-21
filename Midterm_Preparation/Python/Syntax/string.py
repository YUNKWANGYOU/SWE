# ' ' == " "
print('1')
print("1")

# 여러줄 문자열 안되는듯

# 문자열의 접근
a = 'Hello, Dongguk!'
print(a[0])

# 문자열 길이 얻기
print(len(a))

# in/not in 키워드
txt = 'Welcome, Dongguk University Students'
print('Dongguk' in txt) # 참이면 True, 거짓이면 False 출력
print('Welce' in txt)
print("Software Engineering" not in txt)

# 문자열 slicing
print(a[0:5]) # a[0]~a[4]까지 출력
print(a[-5:-2]) # a[-5] 부터 a[-1]까지 출력
 
# 문자열 변경 메소드
# 모든 문자 대문자로 변경
tmp = a.upper()
print(tmp)
# 모든 문자 소문자로 변경
tmp = a.lower()
print(tmp)
# 맨 앞이나 맨 뒤에서의 해당하는 문자열(괄호 안을 공백으로 놔둘 경우 공백) 제거
tmp = a.strip('H')
print(tmp)
# (a,b)일 때 a를 b로 바꿔줌
tmp = a.replace('D','H')
print(tmp)
# 구분 기호를 없애주고 구분기호 기준으로 리스트 반환
tmp = a.split(',')
print(tmp)

# format()함수
quantity = 3
itemno = 567
price = 49.95
name = 'Ipad'
txt = 'I have {}ea of {}. The price of {} which is item #{} is {}$.'
print(txt.format(quantity,name,name,itemno,price))

# Escape character
print(a+'\'')
print(a+'\\')
print(a+'\n')
print('\r'+a)
print('\t'+a)
print(a+'\b'+a)
print(a+'\f'+a)
# print('16\ooo')
# print('15\xhh')