from flask import Flask, jsonify
from http import HTTPStatus

app =  Flask(__name__)

# API 가 있어야 한다. 아래 코드가 API
@app.route('/hithere', methods = ['GET'])  # /hithere 은 경로(port)
def hi_there():
    return 'Hi There'

@app.route('/add',methods = ['GET'])
def add():
    data = 283+111
    return str(data)  # 데이터 리턴할때는 항상 문자영로 만들어서 리턴

@app.route('/',methods = ['GET'])
def root():
    return '안녕하세요'

@app.route('/act/data',methods = ['GET'])
def act():
    ret = {'count':2, 'students': [{'name':'홍길동', 'age':30},{'name':'김나나', 'age':25}]}
    return jsonify(ret)

if __name__ == '__main__':
    app.run()