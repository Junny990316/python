from flask import Flask

app = Flask(__name__) # __name__은 현재 모듈 이름을 의미
@app.route("/")
def hello() :
    return 'Hello. try out Flask'