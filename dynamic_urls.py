from flask import Flask

app = Flask(__name__)


@app.route('/user/<id>/')
def profile_func(id):
    return f"Profile Page of user with id {id}"


if __name__ == '__main__':
    app.run()
