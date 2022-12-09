from flask import Flask


app = Flask(__name__)


@app.route('/')
def some_func():
    return "Hello Flask!"


if __name__ == '__main__':
    app.run()
