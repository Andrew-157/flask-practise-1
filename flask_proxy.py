from flask import Flask, request

app = Flask(__name__)


@app.route('/find/user')
def find_user():
    user_name = request.args.get('name')
    return f"Searching for user {user_name}"


if __name__ == '__main__':
    app.run()
