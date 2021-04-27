from flask import Flask,render_template
app = Flask(__name__)

@app.route('/') 
def hello_dongguk() : 
    return '<h1>윤광이짱</h1><p>너도짱</p>' 

@app.route('/class') # templates 폴더의 html 파일을 참조할 수 있다.
def hello_class() :
    return render_template("class.html")

@app.route('/student/<stdName>')
def hello_std(stdName):
    return render_template("std.html",student = stdName)

@app.route('/score/<int:score>')
def show_score(score):
    return render_template('score.html',marks = score)

@app.route('/score2')
def show_score2():
    score2 = {'Yunkwang':100,'Woongsub' : 0, 'Yejin' :150}
    return render_template('score2.html',score = score2)
if __name__ == '__main__' :
    app.run(debug = True)

