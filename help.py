from flask import Flask


app = Flask(__name__)


@app.route('/')
def func_1():
    return "Home Page"


@app.route('/career/')
def func_2():
    return "Career Page"


@app.route('/feedback/')
def func_3():
    return "Feedback Page"


if __name__ == '__main__':
    app.run()
