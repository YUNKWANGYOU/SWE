# Python 내의 다양한 Loop를 살펴보자.

# while loop
i = 1 
while (i < 6):
    i+=1
    print(i)

# for loop
# 변수 i에 list의 한 요소씩 입력
a = ['math','science','computer']
for i in a :
    print(i)

# 변수 i에 문자열의 한 문자씩 입력
for i in "yunkwang" :
    print(i)

# break : 조건이 만족할 때 loop를 중단시킬 수 있는 능력이 있다. (math, science 까지 출력됨)
for i in a :
    print(i)
    if i == 'science' :
        print("breaked")
        break

# 위의 print문을 아래로 내려보자. (math까지만 출력됨)
for i in a :
    if i == 'science' :
        print("breaked")
        break
    print(i)

# continue문을 사용하면 조건이 만족할 때만 loop를 건너 뛰고 그 다음부터 다시 시작시킬 수 있음 (science 대신 continue 출력)
for i in a :
    if i == 'science' :
        print("continue")
        continue
    print(i)

# 지정된 횟수만큼 반복시키기 위해 range 함수를 사용.
for i in range(10) :
    print(i)

# range(start,end,step)
for i in range(10,0,-2) :
    print(i)

# for loop의 else키워드를 통해 반복문이 끝난 시점에 해야할 행동을 부여할 수 있음
for i in range(6) :
    print(i)
else :
    print('complete')

# for-else-break-continue를 적절히 이용하여 반복문을 구현할 수 있다.
for i in range(6) :
    if i == 4 : break
    print(i)
else :
    print("complete")

# nested loop(중복 for 문)
a = ['one','two','three']
for i in a :
    for j in i :
        print(i,j)

# pass : for문은 비워둘 경우 오류가 발생하므로 아무런 처리를 원하지 않는 for문일 때 pass사용
for x in [0,1,2]:
    pass

