from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods = ['POST','GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.exists("./Flask/4_22/data"):
            os.makedirs('./Flask/4_22/data')
        f.save("./Flask/4_22/data/" + secure_filename(f.filename))
        return 'file uploaded succesfully'

if __name__ == '__main__':
    app.run(debug = True)