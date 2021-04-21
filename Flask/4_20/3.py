from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result() :
    dict = {'YunKwang' : 70 , 'GilDong' : 50, 'Woongsup' : 90}
    return render_template('results.html',result = dict)
    
if __name__ == '__main__':
    app.run(debug=True)