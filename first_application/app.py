import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/test")
def test_function():
    return (
        "Это новая тестовая страничка, ответ сгенерирован в %s"
        % datetime.datetime.now().utcnow()
    )


@app.route("/hello")
def hello_world():
    return (
        "Привет МИР!"
    )


@app.route("/hello/world")
def helloworld():
    return (
        "Hello, world!"
    )


count = 0


@app.route("/counter")
def counter():
    global count
    count += 1
    return (
        f'Данная страница запрашивалась {count} раз'
    )


