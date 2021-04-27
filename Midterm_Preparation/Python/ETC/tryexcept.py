# Python의 try,except 문을 알아보자.

# 출력 결과를 통해 error가 발생했다는 것을 알 수 있음.
try :
    print(x)
except :
    print("exception handling")

# 출력 결과를 통해 NameError가 발생했다는 것을 알 수 있음.
try :
    print(x)
except NameError :
    print("x is not defined.")
except :
    print("other error.")

# try문 실행 후 오류가 발생하지 않으면 else문이 실행된다.
try :
    print('Hello, World!')
except :
    print('exception handling')
else :
    print('No error')

# try문 실행 후 오류 발생 여부에 상관없이 마지막에 finally문을 거친다.
# (1) 에러가 발생하는 경우
try :
    print(x)
except :
    print("Error")
finally :
    print('Final sentence.')

# (2) 에러가 발생하지 않는 경우
try :
    print('Hello, World!')
except :
    print("Error")
finally :
    print('Final sentence.')

# 보통 finally는 특별한 개체를 닫고, 리소스를 정리하는 데 유용하게 쓰인다.
try :
    f = open('demofile.txt')
    f.write('Write demofile.txt.')
except :
    print("Error")
# finally :
#     f.close()

# exception을 일부러 발생시키는 경우. raise 키워드를 사용한다. (주석을 풀고 확인하도록하자.)
# x = -1
# if x < 0 :
#     raise Exception("x is less than 0.")

# x = 'hello'
# if not type(x) is int :
#     raise TypeError("Only Integer number is accepted.")
