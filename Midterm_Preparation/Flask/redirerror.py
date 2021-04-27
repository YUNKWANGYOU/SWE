from flask import Flask,redirect,url_for,render_template,request,abort
app = Flask(__name__)

@app.route('/') 
def index() : 
    return render_template('login2.html')


@app.route('/login',methods = ['GET','POST'])
def login() :
    if request.method == 'POST':
        if request.form['username'] == 'yunkwangzzang' :
            return redirect(url_for('success'))
        else :
            abort(401)

@app.route('/success')
def success():
    return 'Log in Success!'
if __name__ == '__main__' :
    app.run(debug = True)

