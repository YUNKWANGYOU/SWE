from flask import Flask,redirect,url_for,request
app = Flask(__name__)

@app.route('/student/<stdName>') 
def get_hello(stdName):
    return 'get_hello() : Welcome %s!' %stdName

@app.route('/student2/<stdName2>') 
def post_hello(stdName2):
    return 'post_hello() : Welcome %s!' %stdName2

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST' :
        student = request.form['nm']
        return redirect(url_for('post_hello',stdName2 = student))
    elif request.method == 'GET' :
        student = request.args.get('nm')
        return redirect(url_for('get_hello',stdName = student))
if __name__ == '__main__' :
    app.run(debug = True)