# Python의 String format에 대해 배워보자.
# 문자열을 표기하려는 목적으로 format() 메소드를 이용한다.

# 간단한 예 : price를 인수로 넘긴다.
price = 1500
txt = 'Price is {} won'
print(txt.format(price))

# 소수점 이하 두 자리 숫자로 형식을 지정하는 예제
txt = 'Price is {:.2f} won'
print(txt.format(price))

# 다중 인수를 넘기고 싶을 때
name = 'Yunkwang'
grade = 4
year = 2015
txt = "My name is {}, I am {}th grade and admitted in {}."
print(txt.format(name,grade,year))

# {}중괄호에는 index가 붙여지는데 이를 수정할 수도 있다.
txt = "My name is {1}, I am {0}th grade and admitted in {2}."
print(txt.format(name,grade,year))

# {}안에 변수 이름을 지정하여 사용할 수도 있다. 대신 인수로 넘길 때 변수와 변수값 둘다 넘겨줘야한다.
txt = "My name is {grade}, I am {year}th grade and admitted in {name}."
print(txt.format(name = 'Kimyejin',grade = 3,year = 2018))
