from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/') 
def student() : 
    return render_template('student.html')

@app.route('/score',methods = ['GET','POST'])
def score() :
    if request.method == 'POST':
        score = request.form #student.html에서 dict(html에서 name = key, inputtext = value 로 가져와서 score2.html로 dict 전달
        return render_template('score2.html',score = score)

    
if __name__ == '__main__' :
    app.run(debug = True)

