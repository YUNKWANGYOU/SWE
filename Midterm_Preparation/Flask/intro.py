from flask import Flask
app = Flask(__name__)

@app.route('/') # localhost:port/ 로 접속하면,
def hello_dongguk() : # hello_dongguk 함수 자동적으로 실행됨.
    return 'My First Flask Server' # 해당 문자열을 반환함.
    
if __name__ == '__main__' :
    app.run(debug = True)


# from flask import Flask
# app = Flask(__name__)

# @app.route('/') 
# def hello_dongguk() : 
#     return 'My First Flask Server' 
    
# if __name__ == '__main__' :
#     app.run(debug = True)

