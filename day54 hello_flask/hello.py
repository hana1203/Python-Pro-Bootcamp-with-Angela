from flask import Flask
app = Flask(__name__)

# What is this name?
# creating this app from the Flask class
# Flask app initialize하려면 one required input인 import name 필요함

# print(__name__) # __main__ 출력됨
# __name__은 one of special attributes built in to python
# what is current class, function, method, descriptor name 인지 활용 가능
# import해서 쓰는게 아니고 script 형식으로 executed 되는것
# running the code within this file

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return '<h1 style="text-align: center"> Hello, World!</h1>' \
            '<p> I am Injeolmi.</p>' \
            '<img src="https://media1.giphy.com/media/ITacRy2zH4vMQ/giphy.gif?cid=790b7611ae79519adfe442b99afe31e903eb9e354c2185ad&rid=giphy.gif&ct=g">'

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'

## 유저가 입력하는것 어떻게? variable rules
@app.route('/username/<name>/<int:number>')
def great(name, number):
    return f"Hello {name}, you are {number} years old"

if __name__=="__main__":
    app.run()

## debug mode on 하려면?
    app.run(debug=True)
# debug mode 로 할 수 있는것 
# 1. 서버 다시 종료하고 시작안해도 코드 고친것 반영됨
# 2. debug issue

# terminal에서 flask run 치는 것과 같음

##### Setting up the Server?
# To run Flask application, need to import environment variable
# Terminal에서 export FLASK_APP=hello.py 파일이름
# flask run
# enter 치면 아래 실행됨
 # * Serving Flask app 'hello.py' (lazy loading)
 # * Environment: production
 #   WARNING: This is a development server. Do not use it in a production deployment.

# * Running on http://127.0.0.1:5000/
# own 컴퓨터에 로컬 서버 # local address of the website