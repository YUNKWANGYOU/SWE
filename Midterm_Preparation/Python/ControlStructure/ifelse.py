# Python의 조건문이 어떻게 사용되는지 보자.
a = 33
b = 200
if a>b:
    print("a>b")
elif a==b:
    print('a==b')
else :
    print('a<b')

# 실행문이 하나만 있는 경우
if a<b : print("a<b")

# 실행문이 하나인 경우 if else 실행문을 한 줄에 넣을 수 있다.
print("a<b") if a<b else print("아니오")

# 같은 줄에 여러 조건문 사용 가능 -> 안됨
a = 300
b = 300
print('a') if a>b else print("=") if a==b  else print("b")

# and or 연산자를 사용하여 조건문을 결합할 수 있음
a = 200
b = 33
c = 500
if a>b and c>b :
    print("두개의 조건을 모두 만족")
else :
    print("두개 중 하나라도 만족 못시킴.")

# nested if(중복 if문)
x = 40
if x > 10 :
    print("10보다크다.")
    if x>20 :
        print("20보다도 크다.")
    else :
        print("20보다는 작다.")

# pass (if 문은 비울 수 없음. 내용 없는 if 문을 넣기 위해 pass를 사용)
a = 33
b = 200
if b>a:
    pass

