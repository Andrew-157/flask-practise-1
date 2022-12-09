from flask import Flask

app = Flask(__name__)


@app.route('/user/<string:name>/')
def string_func(name):
    return f"Hello {name}"


@app.route('/user/<int:id>/')
def int_func(id):
    return f"Your id is {id}"


if __name__ == '__main__':
    app.run()
