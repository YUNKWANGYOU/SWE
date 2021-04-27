# Python 의 문자열 입력 방법에 대해 배워보자

# input()을 이용하는 방법
username = input("Enter username :")
print("User name is " + username)

# sys.stdin.readline()을 이용하는 방법
import sys
print("Enter username")
username = sys.stdin.readline().rstrip('\n')
print("User name is \n" + username)