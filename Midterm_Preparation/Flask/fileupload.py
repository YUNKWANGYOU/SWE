from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/upload') 
def upload() : 
    return render_template('upload.html')

@app.route('/uploader',methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.exists("./Midterm_Preparation/Flask/data"):
            os.makedirs('./Midterm_Preparation/Flask/data')
        f.save("./Midterm_Preparation/Flask/data/" + secure_filename(f.filename))
        return '파일이 성공적으로 업로드 되었습니다.'
    
if __name__ == '__main__' :
    app.run(debug = True)
