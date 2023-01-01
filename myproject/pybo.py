from flask import Flask
# 플라스크 애플리케이션 생성 코드
# __name__ : 모듈명 = pybo
app = Flask(__name__)


# 플라스크의 데코레이터
@app.route('/')
def hello_pybo():
    return 'hello_pybo'


app.run(debug=True)
