# # Python에서 json은 데이터를 저장하고 교환하는 구문으로 사용한다.
import json

# # json 문자열이 있는 경우 json.loads() 메소드로 읽어온다.
x = '{"name" : "yunkwang","age":26,"sex":"male"}'
# y = json.loads(x)
# # 불러온 값은 dictionary로 받는다.
# print(y['name'])

# -> json.loads() 오류남

y = json.dumps(x)
print(y)