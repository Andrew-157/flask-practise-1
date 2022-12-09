from flask import Flask

app = Flask(__name__)


@app.route('/contact/')
@app.route('/feedback/')
def func():
    return "Feedback Page"


if __name__ == '__main__':
    app.run()
