from flask import Flask

app = Flask(__name__)

# 실행하려면 API 가 있어야 한다! 아래 코드가 API

# client가 '/'에서 GET 메쏘드를 주면 'Hello World' 를 리턴한다.
@app.route('/', methods = ['GET'])   # '/' root 경로
def hello_world():
    return 'Hello World'


if __name__ == '__main__' :
    app.run()