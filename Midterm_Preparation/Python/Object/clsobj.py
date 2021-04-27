# Python의 클래스 오브젝트 이용법
# class
class A:
    x = 10
a = A()
print(a.x)

# __init__() 함수를 통한 초기화
# 함수에 메소드를 넣어보자
class B :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        print("Hello my name is " + self.name)
b = B('yunkwang',26)
print(b.name,b.age)
b.hello()

# 객체 속성의 수정이 가능하다.
b.age = 28
print(b.age)

# 객체 속성을 삭제할 수 있다.
del b.age
# print(b.age) ->오류
b.age = 26

# 내용이 없는 class를 정의할 때 pass사용 (아무 내용 없으면 오류 발생)
class C :
    pass

# class 상속
class Parent:
    def __init__(self,fname,lname):
        self.first = fname
        self.last = lname
    def namePrint(self):
        print(self.first,self.last)
    
d = Parent('Yunkwnag','You')
d.namePrint()

# class() 안에 Parent를 넣어 상속한다.
class Child(Parent) :
    pass
e = Child('Yejin','Kim')
e.namePrint()

# 자식 class에 __init__()함수를 추가하면 클래스를 재정의 하므로 부모클래스를 더이상 상속하지 않는다.
# 재정의하지 않고 상속을 유지하고 싶다면 __init__()함수안에 __init__()함수를 정의한다.
class Child2(Parent) :
    def __init__(self,fname,lname) :
        Parent.__init__(self,fname,lname)
f = Child2('Yejin','Kim')
f.namePrint()

# super()의 사용 : 자식 class가 부모 class의 모든 method와 속성을 상속하도록한다.
# 속성을 추가할 수도 있다.
class Child3(Parent):
    def __init__(self,fname,lname) :
        super().__init__(fname,lname)
        self.graduationyear = 2021

g = Child3('yunkwnag','you')
print(g.graduationyear)

# 속성값을 매개변수로 전달하여 추가도 가능
class Child4(Parent):
    def __init__(self,fname,lname,year) :
        super().__init__(fname,lname)
        self.graduationyear = year
h = Child4('yunkwang','you',2022)
print(h.first,h.last,h.graduationyear)

# 상속된 class에 메소드를 새로 추가해보자.
class Child5(Parent) :
    def __init__(self,fname,lname,year) :
        super().__init__(fname,lname)
        self.graduationyear = year
    def welcome(self):
        print('Welcome',self.first,self.last,'to the class of',self.graduationyear)

i = Child5('yunkwang','you','2021')
i.welcome()
