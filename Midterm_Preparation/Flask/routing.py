from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_dongguk() : 
    return 'My First Flask Server' 

@app.route('/hello')
def hello():
    return 'Hello'

# def hello2():
#     return 'Hello2'
# app.add_url_rule('/','hello2',hello2)
# ->app.add.url_rule 잘 안되는것 확인했음
if __name__ == '__main__' :
    app.run(debug = True)
