from flask import Flask
app = Flask(__name__)

@app.route('/<name>') # name변수를 hello_dongguk의 매개변수로 넘김
def hello_dongguk(name) : # url로부터 인수를 전달받았음
    return 'My Name is %s' %name # 반환하면서 표시해줌

@app.route('/<int:stdID>') # 정수형 변수를 입력해주면 hello_int 함수가 실행됨
def hello_int(stdID) :
    return 'My stdID is %d' %stdID

@app.route('/<float:score>') # 실수형 변수를 입력해주면 hello_float 함수가 실행됨
def hello_float(score) :
    return 'My score is %f' %score

@app.route('/home') # http://localhost:port/home/ 으로 검색하면 마지막 '/' 때문에 오류남
def home():
    return 'Home'

@app.route('/home2/') # http://localhost:port/home/ 으로 검색해도 이미 마지막에 '/'를 지정해줘서 오류가 나지 않는다.
def home2():
    return 'Home2'

if __name__ == '__main__' :
    app.run(debug = True)
