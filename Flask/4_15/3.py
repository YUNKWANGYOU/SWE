from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_ice2(name):
   return '2015112173 유윤광<br>Hello ICE students %s' %name

if __name__ == '__main__':
   app.run(debug=True)


