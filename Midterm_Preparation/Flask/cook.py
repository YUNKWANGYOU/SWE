from flask import Flask,render_template,request,make_response
app = Flask(__name__)

@app.route('/') 
def homepage() : 
    return render_template('homepage.html')

@app.route('/setcookie',methods=['GET','POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['username']
    # 아래 세 줄은 쿠키를 생성하는 절차    
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userName',user)
    return resp

@app.route('/getcookie')
def getcookie():
    # 생성 돼있는 쿠키를 읽어와보자.
    name = request.cookies.get('userName')
    return '<h1>Welcome' + name + '!</h1>'
    
if __name__ == '__main__' :
    app.run(debug = True)

