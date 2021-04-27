# regex는 정규식을 의미한다.
import re
txt = 'The rain in Seoul'
# search()함수는 찾고싶은 문자열이 해당하는 문자열 안에 포함돼있는지 확인해준다.
x = re.search("^The.*Seoul$",txt)

print(x)

x = re.findall('e',txt) # 첫 e 두번재 e 두 개 반환
print(x)

x = re.search('\s',txt) # 첫번째 공백의 위치
print(x)
print(x.start())

x = re.search('Rain',txt) # 대소문자도 구분해주어야함
print(x)

x = re.split('\s',txt) # 공백을 기준으로 분할된 List를 반환한다.
print(x)

x = re.split('\s',txt,1) # 세 번째 인수는 분할 횟수를 나타낸다.
print(x)

x = re.sub('\s','9',txt) # 맨 처음의 인수 대신 두번째 인수를 써서 표현해준다.
print(x)

x = re.sub('\s','9',txt,2)
print(x) # 네 번째 인수는 바꿔치기할 문자의 개수를 나타낸다.

x = re.search(r"\bS\w+",txt) # 대문자 S로 시작하는 모든 단어를 찾는다.
print(x)

print(x.string) # 함수에 전달 된 문자열을 인쇄한다. -> txt 전체가 인쇄됨

print(x.group()) # Matching된 문자열 부분만 반환한다.