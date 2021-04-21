from flask import Flask

app = Flask(__name__)

@app.route('/hello/<int:stdID>')
def hello_ice(stdID):
   return '2015112173 유윤광<br>Hello ICE students %d' %stdID

@app.route('/flt/<float:float>')
def floatNum(float):
   return '2015112173 유윤광<br>The number is %f!' %float

if __name__ == '__main__':
   app.run(debug=True)


