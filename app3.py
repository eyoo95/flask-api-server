from flask import Flask, request, jsonify
from http import HTTPStatus

app = Flask(__name__)

@app.route('/add_two_nums',methods = {'POST'})  # 웹브라우저는 GET 메소드로 호출한다.
def add():
    # 클라이언트로 두 수를 받는다.
    data = request.get_json()
    ret = data['x'] + data['y']
    result = {"result" : ret}

    return jsonify(result)


if __name__ == '__main__':
    app.run()

