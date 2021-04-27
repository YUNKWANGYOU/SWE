from flask import Flask,session,redirect,url_for,escape,request
app = Flask(__name__)
app.secret_key='yunkwangzzang'
@app.route('/') 
def index() : 
    if 'username' in session :
        username = session['username']
        return username + "으로 로그인 되었습니다.<br><b><a href = '/logout'>로그아웃하려면 클릭해주세요.</b></a>"
    
    return "로그인 되어있지 않습니다. <br><a href = '/login'></b>로그인하려면 클릭해주세요"

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST' :
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return "<form class='' action='' method='post'><p><input type='text' name='username' value=''></p><p><input type='submit' name='' value='로그인'></p></form>"
if __name__ == '__main__' :
    app.run(debug = True)
